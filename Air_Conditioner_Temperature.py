# Time Complexity: O(T)
# Space Complexity: O(1)

T = int(input())  # Number of test cases

for i in range(T):
    # Read three integers A, B, and C
    A, B, C = map(int, input().split())

    # Check if B is greater than or equal to both A and C
    if A <= B and B >= C:
        print("YES")
    else:
        print("NO") 
