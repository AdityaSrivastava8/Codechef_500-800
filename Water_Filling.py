T = int(input())  # Read the number of test cases

for character in range(T):  # Loop over each test case
    A, B, C = map(int, input().split())  # Read three integers A, B, C

    D = A + B + C  # Calculate the sum of A, B, and C

    if D == 2 or D == 3:  # If the sum is 2 or 3
        print("Not now")  # Condition satisfied for 'Not now'
    else:
        print("Water filling time")  # Otherwise, it's 'Water filling time'

# Time Complexity: O(T) -> Each test case is processed in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
