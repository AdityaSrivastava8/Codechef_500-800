import math  # Import math module for the ceil() function

T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    N, X = map(int, input().split())  # Read total quantity N and cost/value X

    N = math.ceil(N / 6)  # Calculate the number of groups of size 6 (round up for incomplete groups)

    print(N * X)  # Output the total cost/value for all groups

# Time Complexity: O(T) -> Each test case runs in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
