# Python Bug: ZeroDivisionError in Average Calculation

This repository demonstrates a common Python bug: a `ZeroDivisionError` that occurs when trying to calculate the average of an empty list. The `calculate_average` function does not handle the case where the input list is empty, resulting in a division by zero error.  A solution is provided to handle this edge case gracefully.

## Bug

The `bug.py` file contains the erroneous `calculate_average` function which causes a `ZeroDivisionError` when presented with an empty list. 

## Solution

The `bugSolution.py` file demonstrates a corrected `calculate_average` function.  It now explicitly checks for an empty input list and returns 0 in that scenario, preventing the `ZeroDivisionError`. This approach avoids the exception and provides a more robust solution.