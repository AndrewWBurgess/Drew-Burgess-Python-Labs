import time
import random
import requests
import json
import csv
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# User Agent from Chrome Browser on Win 10/11
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

DEFAULT_SLEEP = 0.1  # These may need tuning
SIGMA = 0.1

DOMAIN = 'http://books.toscrape.com'  # Ideally, these would be
STATE_FILENAME = 'state.json'         # read in from a configuration
OUTPUT_FILENAME = 'books.csv'         # or command line, but this is fine


def get(url: str) -> requests.Response:
    """Waits a random amount of time, then send a GET request"""
    time.sleep(abs(random.gauss(DEFAULT_SLEEP, SIGMA)))
    return requests.get(url, headers=HEADERS)


def save_state(filename: str, links: list[str], data: dict[str, dict]) -> None:
    """Save links left to visit and the data extracted to a JSON file"""
    state = {'links_to_process': links, 'processed_data': data}
    try:
        with open(filename, 'w') as file:
            json.dump(state, file, indent=4)
    except IOError as e:
        print(f"Error saving state to {filename}: {e}")


def load_state(filename: str) -> tuple[list[str], dict[str, dict]]:
    """Load links left to visit and collected data from a JSON file"""
    try:
        with open(filename, 'r') as file:
            state = json.load(file)
            links_to_process = state.get('links_to_process', [])
            processed_data = state.get('processed_data', {})
        return links_to_process, processed_data
    except (IOError, FileNotFoundError) as e:
        print(f"Error loading state from {filename}: {e}")
        return [], {}


def write_spreadsheet(filename: str, data: dict[str, dict], default_headers: list[str] = None) -> None:
    """Write all data to a CSV file"""
    if not data:
        headers = default_headers if default_headers else ["title", "price", "rating"]  # Specify any desired headers here
    else:
        
        headers = set()
        for row in data.values():
            headers.update(row.keys())
        headers = list(headers)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for row in data.values():
            if row:  # Check if row has content
                writer.writerow(row)


if __name__ == '__main__':
    to_visit: list
    data: dict[str, dict]
    to_visit, data = load_state(STATE_FILENAME)
    if not to_visit:
        to_visit = [urljoin(DOMAIN, '/index.html')]

    # Main Loop
    while len(to_visit) > 0:
        try:
            current_url = to_visit.pop(0)
            if current_url in data:
                continue
            response = get(current_url)
            if response.status_code != 200:
                print(f"Failed to retrieve {current_url}")
                to_visit.insert(0, current_url)
                continue 
            soup = BeautifulSoup(response.text, 'html.parser')
            book_data = {}
            try:
                book_data['title'] = soup.find('h1').text.strip()
                book_data['price'] = soup.find(class_='price_color').text.strip()
                book_data['rating'] = soup.find(class_='star-rating')['class'][1]
                if book_data:
                    print("Adding book data:", book_data)  # Debugging line
                    data[current_url] = book_data
            except AttributeError:
                
                data[current_url] = {}

            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    next_url = urljoin(current_url, href)
                    next_url = next_url.split('#')[0]
                    if next_url not in data and next_url not in to_visit and next_url.startswith(DOMAIN):
                        to_visit.append(next_url)
            save_state(STATE_FILENAME, to_visit, data)
        except KeyboardInterrupt:
            save_state(STATE_FILENAME, to_visit, data)
            is_finished = False
            print("Process interrupted by user. State saved.")
            break
    else:
        is_finished = True
    if is_finished:
        write_spreadsheet(OUTPUT_FILENAME, data)
        print(f"Data collection complete. Results written to {OUTPUT_FILENAME}.")
