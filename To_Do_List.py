# Time Complexity: O(N) per test case
# Overall Time Complexity: O(ΣN) for all test cases
#
# Space Complexity: O(N)
# (The list D stores N integers)

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the number of elements
    N = int(input())

    # Read the list of integers
    D = list(map(int, input().split()))

    # Counter for elements greater than or equal to 1000
    count = 0

    # Traverse the list and count valid elements
    for i in range(N):
        if D[i] >= 1000:
            count += 1

    # Print the result for the current test case
    print(count)
