# Read the number of test cases
T = int(input())

# Process each test case
for i in range(T):

    # Read X, A, and B
    # X = required score
    # A = number of 1-point problems solved
    # B = number of 2-point problems solved
    X, A, B = map(int, input().split())

    # Calculate the total score obtained
    total_score = (A * 1) + (B * 2)

    # Check if the obtained score is enough to qualify
    if X <= total_score:
        print("Qualify")
    else:
        print("NotQualify")

# Time Complexity:
# O(T)
# For each test case, only a few arithmetic operations and comparisons are performed.

# Space Complexity:
# O(1)
# Only a constant amount of extra space is used.
