# Function: create_combination_table
Purpose:

This function generates a Pandas DataFrame that contains all possible combinations of the input string variables. The DataFrame will include columns for each variable and an additional column that indicates whether all the values in a row are identical.

Parameters:

Input: Accepts one or more string variables as arguments.
Output:

Pandas DataFrame:
Columns are named sequentially as A0, A1, A2, ..., based on the number of input variables.
An additional column, is_identical, is included, where:
True: All values in the row are identical.
False: Values in the row differ.
Example:

| A0    | A1    | A2    | is_identical |
|-------|-------|-------|--------------|
| apple | apple | apple | True         |
| apple | apple | banana| False        |
| apple | banana| apple | False        |
| apple | banana| banana| False        |
| banana| apple | apple | False        |
| banana| apple | banana| False        |
| banana| banana| apple | False        |
| banana| banana| banana| True         |


If the input strings are "apple", "banana", and "apple", the function will return a DataFrame like this:

