T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    X, Y, Z = map(int, input().split())  # Read three integers: X, Y, Z

    E = X * Y  # Calculate the product of X and Y

    P = (Z / E) * 100  # Calculate percentage of Z with respect to E

    if P > 50:  # If percentage is greater than 50
        print("YES")  # Condition satisfied
    else:
        print("NO")  # Condition not satisfied

# Time Complexity: O(T) -> Each test case takes constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
