
This program and documentation describe 5 functions created with general use that can not be accessed with basic functions or the standard library. Each function in the library has below it some documentation, including descriptions of its purpose, conditions, complexity and use cases.


## 1. Timer function

### Description

The `timer` function measures and prints the execution time of a function.
### Algorithm

1. Record the time before calling the function
2. execute the function
3. calculate the elapsed time
4. print
### Pre-Conditions
- must be a callable function


### Post-Conditions
- Prints the time to the console



### Complexity

- Time Complexity: O(1)O(1) (aside from the function execution time.)
- Space Complexity: O(1)O(1).

### Typical Use Cases

- Measuring the performance of functions.
- Debugging performance bottlenecks.

---

## 2. Dictionary Merger

### Description

The `merge_dicts_default` function merges two dictionaries, and also allows the user to decide what will occur in the event of a duplicate (by default it prioritizes the second value.)

### Algorithm

1. Copy the first dictionary.
2. Iterate through the key-value pairs of the second dictionary.
3. Add or update the key in the copied dictionary based on the conflict resolution strategy.

### Pre-Conditions

- Inputs must be dictionaries.

### Post-Conditions

- Returns a merged dictionary without modifying the original inputs.

### Complexity

- Time Complexity: O(n)O(n), where n is the total number of keys in both dictionaries.
- Space Complexity: O(n)O(n), for the merged dictionary.

### Typical Use Cases

- Combining data from multiple sources.

---

## 3. CSV Column Extractor

### Description

The `extract_csv_columns` function takes inputted columns from a csv file and turns them into a list of lists.

### Algorithm

1. Open the CSV file for reading.
2. Use `csv.reader` to parse the file.
3. Go through each row, extracting the inputted columns.
4. Append results list with the columns from step 3.

### Pre-Conditions

- The file must exist and be in CSV format.
- Column indices must be valid integers.

### Post-Conditions

- Returns a list of lists containing the extracted columns.

### Complexity

- Time Complexity: O(r⋅c)O(r \cdot c), where rr is the number of rows and cc is the number of columns.
- Space Complexity: O(r⋅c)O(r \cdot c).

### Typical Use Cases

- Extracting headers or a specific set of 
- This one would have been really useful for the counties lab

---

## 4. Fibonacci Sequence Generator

### Description

The `generate_fibonacci` function generates a Fibonacci sequence with n terms.

### Algorithm

1. Return an empty list if the input n is less than 1
2. Return [0] if n is 1.
3. Initialize the sequence with [0, 1].
4. continue to compute the next terms by summing the last two terms in the sequence until n is reached.

### Pre-Conditions

- Input n must be a non-negative integer.

### Post-Conditions

- Returns a list containing n terms of the Fibonacci sequence.

### Complexity

- Time Complexity: O(n)O(n).
- Space Complexity: O(n)O(n).

### Typical Use Cases

- Generating number sequences for mathematical problems that require the Fibonacci sequence

---

## 5. Add Dictionaries Function

### Description


The `merge_dicts_with_sum` function merges two dictionaries, similar to the `merge_dicts_default` but instead of replacing one with another it adds the value of the 1st and 2nd dictionary.

### Algorithm

1. Copy the first dictionary.
2. Iterate through the key-value pairs of the second dictionary.
3. add the values together for repeats and append it to the new dictionary, or add the only value if it is what remains.

### Pre-Conditions

- Inputs must be dictionaries.
- Input values must be numberic

### Post-Conditions

- Returns a merged and added dictionary without modifying the original inputs.

### Complexity

- Time Complexity: O(n)O(n), where n is the total number of keys in both dictionaries.
- Space Complexity: O(n)O(n), for the merged dictionary.

### Typical Use Cases

- Combining successive data to create sums.
- Example: find the total rainfall over a number of regions when given yearly amounts
---
