import math  # Import math module for using ceil() function

T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    N, X = map(int, input().split())  # Read total number N and already completed X

    A = (N - X) / 4  # Calculate remaining quantity divided into groups of 4

    if A <= 0:  # If no groups are left or value is negative
        print(0)  # Output 0
    else:
        print(math.ceil(A))  # Round up and print the number of groups needed

# Time Complexity: O(T) -> Each test case is processed in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
