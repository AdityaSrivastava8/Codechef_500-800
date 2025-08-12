T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    A, B, C = map(int, input().split())  # Read three integers A, B, and C

    D = (A + B) / 2  # Calculate the average of A and B

    if D > C:  # If the average is greater than C
        print("YES")  # Condition satisfied
    else:
        print("NO")  # Condition not satisfied

# Time Complexity: O(T) -> Each test case takes constant time
# Space Complexity: O(1) -> Uses only a constant amount of extra space
