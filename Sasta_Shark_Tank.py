# Read the number of test cases
T = int(input())

# Process each test case
for i in range(T):

    # Read A and B from the same line
    A, B = map(int, input().split())

    # Compare the effective values
    if A * 100 / 10 > B * 100 / 20:
        print("FIRST")      # First option is better

    elif A * 100 / 10 < B * 100 / 20:
        print("SECOND")     # Second option is better

    else:
        print("ANY")        # Both options are equally good

# Time Complexity:
# O(T)
# Each test case performs only a constant number of arithmetic operations.

# Space Complexity:
# O(1)
# Only a few variables (A, B) are used.
