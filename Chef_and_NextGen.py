T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    A, B, X, Y = map(int, input().split())  # Read four integers: A, B, X, Y

    # Need: total quantity required
    N = A * B  

    # Capacity: total quantity available
    C = X * Y    

    if C >= N:  # If capacity equals or exceeds the need
        print("YES")  # Condition satisfied
    else:
        print("NO")  # Condition not satisfied

# Time Complexity: O(T) -> Each test case runs in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
