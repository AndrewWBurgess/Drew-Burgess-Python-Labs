
def format_cell(item, width):
    """Format a cell for display in a table.

    Args:
        item: The item to format (str, int, float, bool, or None).
        width: The width to which the cell should be formatted.

    Returns:
        A formatted string representation of the item.
    """
    if isinstance(item, str):
        return str(item).ljust(width)
    elif isinstance(item, (int, float)):
        return str(item).rjust(width)
    elif isinstance(item, bool):
        return str(item).center(width)
    elif item is None:
        return ' ' * width
    else:
        raise Exception("Unsupported data type")


def create_table(header, data):
    """Create a formatted table from headers and data.

    Args:
        header: A list of column headers.
        data: A list of lists containing the data for each row.

    Returns:
        A string representation of the formatted table.
    """
    if len(header) == 0 or any(len(row) != len(header) for row in data):
        raise Exception("length of headers does not equal length of data")
    column_widths = [max(len(str(item)) for item in col) for col in zip(header, *data)]
    header_row = '| ' + ' | '.join(f"{str(h).ljust(w)}" for h, w in zip(header, column_widths)) + ' |'
    separator_row = '| ' + ' | '.join('-' * w for w in column_widths) + ' |'
    data_rows = []
    for row in data:
        formatted_row = '| ' + ' | '.join(format_cell(item, w) for item, w in zip(row, column_widths)) + ' |'
        data_rows.append(formatted_row)
    table = [header_row, separator_row] + data_rows
    return '\n'.join(table)


def create_table_from_dicts(data, header=None):
    """Create a formatted table from a list of dictionaries.

    Args:
        data: A list of dictionaries containing row data.
        header: An optional list of column headers.

    Returns:
        A string representation of the formatted table.
    """
    if header is None:
        if data:
            header = list(data[0].keys())
        else:
            return []
    column_widths = [max(len(str(h)), max(len(str(row.get(h, ""))) for row in data)) for h in header]
    header_row = '| ' + ' | '.join(f"{str(h).ljust(w)}" for h, w in zip(header, column_widths)) + ' |'
    separator_row = '| ' + ' | '.join('-' * w for w in column_widths) + ' |'
    data_rows = []
    for row in data:
        formatted_row = '| ' + ' | '.join(format_cell(row.get(h, ""), w) for h, w in zip(header, column_widths)) + ' |'
        data_rows.append(formatted_row)
    return '\n'.join([header_row, separator_row] + data_rows)


def merge_sorted_lists(*lists):
    """Merge multiple sorted lists into a single sorted list.

    Args:
        *lists: Variable number of sorted lists to merge.

    Returns:
        A single merged and sorted list containing all elements.
    """
    pointers = [0] * len(lists)
    merged_list = []
    while True:
        smallest_value = None
        smallest_index = -1
        for i in range(len(lists)):
            if pointers[i] < len(lists[i]):
                if smallest_value is None or lists[i][pointers[i]] < smallest_value:
                    smallest_value = lists[i][pointers[i]]
                    smallest_index = i
        if smallest_index == -1:
            break
        merged_list.append(smallest_value)
        pointers[smallest_index] += 1
    return merged_list


def caesar(plaintext, n=13):
    """Encrypt a plaintext using the Caesar cipher.

    Args:
        plaintext: The text to encrypt.
        n: The number of positions to shift each letter (default is 13).

    Returns:
        The encrypted text as a string.
    """
    lc_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    uc_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lc_caesarbet = lc_alphabet[n:27:1] + lc_alphabet[0:n:1]
    uc_caesarbet = uc_alphabet[n:27:1] + uc_alphabet[0:n:1]
    result = ''
    for char in plaintext:
        if char in lc_alphabet:
            index = lc_alphabet.index(char)
            result += lc_caesarbet[index]
        elif char in uc_alphabet:
            index = uc_alphabet.index(char)
            result += uc_caesarbet[index]
        else:
            result += char
    return result


