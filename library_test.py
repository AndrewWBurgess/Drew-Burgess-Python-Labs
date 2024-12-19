# library_test

import os
from library import timer, merge_dicts_default, extract_csv_columns, generate_fibonacci, merge_dicts_with_sum

def test_timer():
    """Test the timer decorator."""
    @timer
    def dummy_function(x):
        return x * 2

    result = dummy_function(5)
    assert result == 10
    print("test_timer passed.")

def test_merge_dicts_default():
    """Test the merge_dicts_default function."""
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}

    # Prefer values from the second dictionary
    merged = merge_dicts_default(dict1, dict2, prefer_second=True)
    assert merged == {"a": 1, "b": 3, "c": 4}

    # Prefer values from the first dictionary
    merged = merge_dicts_default(dict1, dict2, prefer_second=False)
    assert merged == {"a": 1, "b": 2, "c": 4}

    print("test_merge_dicts_default passed.")

def test_extract_csv_columns():
    """Test the extract_csv_columns function."""
    test_csv_path = "test.csv"
    test_data = """col1,col2,col3\n1,2,3\n4,5,6\n7,8,9"""

    with open(test_csv_path, "w") as f:
        f.write(test_data)

    result = extract_csv_columns(test_csv_path, [0, 2])
    assert result == [["col1", "col3"], ["1", "3"], ["4", "6"], ["7", "9"]]

    os.remove(test_csv_path)
    print("test_extract_csv_columns passed.")

def test_generate_fibonacci():
    """Test the generate_fibonacci function."""
    assert generate_fibonacci(0) == []
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    print("test_generate_fibonacci passed.")

def test_merge_dicts_with_sum():
    """Test the merge_dicts_with_sum function."""
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}

    merged = merge_dicts_with_sum(dict1, dict2)
    assert merged == {"a": 1, "b": 5, "c": 4}

    dict3 = {"d": 5.5}
    dict4 = {"d": 4.5}

    merged = merge_dicts_with_sum(dict3, dict4)
    assert merged == {"d": 10.0}

    print("test_merge_dicts_with_sum passed.")

def run_tests():
    """Run all test functions."""
    test_timer()
    test_merge_dicts_default()
    test_extract_csv_columns()
    test_generate_fibonacci()
    test_merge_dicts_with_sum()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
