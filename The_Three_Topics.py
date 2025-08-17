A, B, C, X = map(int, input().split())  # Read 4 integers from input

# Check if X matches any of A, B, or C
if A == X or B == X or C == X:
    print("YES")   # If any match is found
else:
    print("NO")    # If no match is found

# Time Complexity: O(1) -> Constant number of comparisons
# Space Complexity: O(1) -> Only a few integer variables used
