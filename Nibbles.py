# Read the number of test cases
T = int(input())

# Process each test case
for i in range(T):

    # Read the number
    N = int(input())

    # Check if N is divisible by 2
    if N % 2 == 0:
        print("GOOD")      # N is even
    else:
        print("NOT GOOD")  # N is odd

# Time Complexity:
# O(T)
# Each test case performs one modulo operation and one comparison.

# Space Complexity:
# O(1)
# Only a single variable (N) is used regardless of input size.
