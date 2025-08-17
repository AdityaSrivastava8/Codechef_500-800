T = int(input())  # Read the number of test cases

for i in range(T):  # Loop through all test cases
    A, B = map(int, input().split())  # Read first pair of integers
    C, D = map(int, input().split())  # Read second pair of integers
    
    # Check if both A <= C and B <= D
    if A <= C and B <= D:
        print("POSSIBLE")  # Condition satisfied
    else:
        print("IMPOSSIBLE")  # Condition not satisfied

# Time Complexity: O(T) -> Each test case takes constant time O(1)
# Space Complexity: O(1) -> Only a few integer variables are used
