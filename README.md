# fact
Python script to calculate the factorial of a non-negative integer
In this script:

The factorial function takes a non-negative integer n.
If n is 0, it returns 1 (the base case).
Otherwise, it returns n multiplied by the factorial of n-1, which is calculated by recursively calling the factorial function with n-1.
The recursion continues until it reaches the base case (n = 0), at which point it starts returning values back up the call stack.
The result is the factorial of the original n.
This script demonstrates how recursion can be used to elegantly solve problems by breaking them down into smaller, simpler subproblems. However, it's important to note that recursion can be less efficient in some cases compared to iterative solutions and may lead to stack overflow errors for large inputs.
