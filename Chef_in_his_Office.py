T = int(input())  # Read the number of test cases

for character in range(T):  # Loop over each test case
    X, Y = map(int, input().split())  # Read two integers: X and Y

    P = X * 4  # Multiply X by 4 and store in P

    print(Y + P)  # Output the sum of Y and P

# Time Complexity: O(T) -> Each test case runs in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
