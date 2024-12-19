# library

import os
import time
import random
import csv
from typing import Callable, Any, List, Dict, Optional, Iterator

# 1. Function Timer
def timer(func: Callable) -> Callable:
    """
    A decorator to measure and print the execution time of a function,
    with exception handling.

    Args:
        func (Callable): The function to time.

    Returns:
        Callable: A wrapper function with timing functionality.
    """
    def wrapper(*args, **kwargs) -> Any:
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            print(f"{func.__name__} executed in {elapsed_time:.2f} seconds.")
            return result
        except Exception as e:
            print(f"Error while executing {func.__name__}: {e}")
            raise
    return wrapper


# 2. Dictionary Merger
def merge_dicts_default(dict1: Dict[Any, Any], dict2: Dict[Any, Any], prefer_second: bool = True) -> Dict[Any, Any]:
    """
    Merges two dictionaries with a default conflict resolution strategy,
    with exception handling.

    Args:
        dict1 (Dict[Any, Any]): First dictionary.
        dict2 (Dict[Any, Any]): Second dictionary.
        prefer_second (bool): If True, values from dict2 will override values in dict1 during conflicts.
                              If False, values from dict1 will be kept during conflicts.

    Returns:
        Dict[Any, Any]: Merged dictionary.
    """
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Both arguments must be dictionaries.")

    merged = dict1.copy()
    try:
        for key, value in dict2.items():
            if key in merged:
                if prefer_second:
                    merged[key] = value
            else:
                merged[key] = value
    except Exception as e:
        print(f"Error during merging: {e}")
        raise
    return merged


# 3. CSV Column Extractor
def extract_csv_columns(file_path: str, columns: List[int]) -> List[List[str]]:
    """
    Returns specific columns from a CSV file, with exception handling.

    Args:
        file_path (str): Path to the CSV file.
        columns (List[int]): List of column indices to extract.

    Returns:
        List[List[str]]: Extracted columns as lists of strings.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    extracted_data = []
    try:
        with open(file_path, mode='r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                try:
                    extracted_data.append([row[col] for col in columns])
                except IndexError as e:
                    print(f"Index error for row {row}: {e}")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        raise
    return extracted_data


# 4. Fibonacci Sequence Generator
def generate_fibonacci(n: int) -> List[int]:
    """
    Generates a Fibonacci sequence with n terms, with exception handling.

    Args:
        n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
        List[int]: A list containing the Fibonacci sequence up to n terms.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    try:
        if n == 0:
            return []
        if n == 1:
            return [0]
        sequence = [0, 1]
        for _ in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
    except Exception as e:
        print(f"Error generating Fibonacci sequence: {e}")
        raise


# 5. Merge Dictionaries with Summation
def merge_dicts_with_sum(dict1: Dict[Any, int], dict2: Dict[Any, int]) -> Dict[Any, int]:
    """
    Merges two dictionaries, summing values for keys that appear in both,
    with exception handling for invalid data types.

    Args:
        dict1 (Dict[Any, int]): The first dictionary.
        dict2 (Dict[Any, int]): The second dictionary.

    Returns:
        Dict[Any, int]: A new dictionary with merged values.

    Raises:
        ValueError: If non-numeric values are found in the dictionaries.
    """
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("Both arguments must be dictionaries.")

    merged = dict1.copy()

    for key, value in dict2.items():
        try:
            if key in merged:
                if not isinstance(value, (int, float)) or not isinstance(merged[key], (int, float)):
                    raise ValueError(f"Non-numeric value encountered for key '{key}'.")
                merged[key] += value
            else:
                if not isinstance(value, (int, float)):
                    raise ValueError(f"Non-numeric value encountered for key '{key}'.")
                merged[key] = value
        except Exception as e:
            print(f"Error processing key '{key}': {e}")
            continue
    return merged
