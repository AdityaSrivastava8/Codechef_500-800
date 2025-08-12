import math  # Import math module for the ceil() function

T = int(input())  # Read the number of test cases

for i in range(T):  # Loop over each test case
    N, X = map(int, input().split())  # Read N and X from input

    ans = (N * X) / 4  # Calculate (N * X) divided by 4

    print(math.ceil(ans))  # Output the ceiling value of ans

# Time Complexity: O(T) -> Each test case is processed in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
