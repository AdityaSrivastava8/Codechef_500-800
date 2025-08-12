T = int(input())  # Read the number of test cases

for character in range(T):  # Loop over each test case
    X = int(input())  # Read the integer value X

    if X <= 100:  # Case 1: X is 100 or less
        print(X)  # No change applied
    elif 100 < X and X <= 1000:  # Case 2: X is between 101 and 1000
        print(X - 25)  # Subtract 25
    elif 1000 < X and X <= 5000:  # Case 3: X is between 1001 and 5000
        print(X - 100)  # Subtract 100
    else:  # Case 4: X is greater than 5000
        print(X - 500)  # Subtract 500

# Time Complexity: O(T) -> Each test case runs in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
