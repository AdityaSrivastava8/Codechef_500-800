T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    X = int(input())  # Read the input integer X

    Y = X + 3  # Add 3 to X and store the result in Y

    if Y <= 10:  # Check if Y is less than or equal to 10
        print("YES")  # Condition satisfied
    else:
        print("NO")  # Condition not satisfied

# Time Complexity: O(T) -> Each test case takes constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
