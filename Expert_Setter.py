T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    X, Y = map(int, input().split())  # Read two integers X and Y

    Z = (Y / X) * 100  # Calculate Y as a percentage of X

    if Z >= 50:  # If the percentage is at least 50
        print("Yes")  # Condition satisfied
    else:
        print("No")  # Condition not satisfied

# Time Complexity: O(T) -> Each test case runs in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
