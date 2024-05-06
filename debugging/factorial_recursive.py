#!/usr/bin/python3
import sys

# Define a function to calculate the factorial of a number recursively
def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: multiply n by the factorial of (n-1)
else:
    return n * factorial(n-1)

# Get the command-line argument and calculate its factorial
# Note: sys.argv[0] contains the script name, so we use sys.argv[1] for the argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
