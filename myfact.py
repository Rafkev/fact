def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    - n: The non-negative integer to calculate the factorial of.

    Returns:
    - The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
n = 5
print(f"The factorial of {n} is {factorial(n)}")
