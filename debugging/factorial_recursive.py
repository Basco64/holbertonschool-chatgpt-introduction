#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer recursively.

    Function Description:
    This function calculates the factorial of a given non-negative integer `n`. 
    The factorial of `n` (denoted as `n!`) is the product of all positive integers 
    from 1 to `n`. By definition, the factorial of 0 is 1.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer `n`. If `n` is 0, it returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the input number from command line arguments
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
