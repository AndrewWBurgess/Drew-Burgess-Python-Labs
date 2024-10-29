from lab7 import format_cell, merge_sorted_lists, caesar

def test_format_cell():
    """Test the format_cell function."""
    assert format_cell("Hello", 10) == "Hello     "
    assert format_cell(123, 5) == "  123"
    assert format_cell(True, 5) == " True"
    assert format_cell(None, 5) == "     "
    print("format_cell tests passed.")


def test_merge_sorted_lists():
    """Test the merge_sorted_lists function."""
    list1 = [1, 4, 6]
    list2 = [2, 3, 5]
    list3 = [0, 7, 8]
    expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_sorted_lists(list1, list2, list3) == expected_output
    print("merge_sorted_lists tests passed.")


def test_caesar():
    """Test the caesar function."""
    assert caesar("Hello, World!", 3) == "Khoor, Zruog!"
    assert caesar("abc XYZ", 1) == "bcd YZA"
    assert caesar("123! @#", 4) == "123! @#"
    assert caesar("", 5) == ""
    print("caesar tests passed.")


def run_tests():
    test_format_cell()
    test_merge_sorted_lists()
    test_caesar()

run_tests()