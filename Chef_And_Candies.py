# cook your dish here 
import math  # Importing math module for the ceil() function

T = int(input())  # Read the number of test cases
for _ in range(T):  # Loop over each test case
    N, X = map(int, input().split())  # Read total number N and already completed X

    A = (N - X) / 4  # Calculate how many full groups of 4 are left after X

    if A <= 0:  # If no groups left or negative (already done), print 0
        print(0)
    else:
        print(math.ceil(A))  # Round up to account for partial groups

# Time Complexity: O(T) -> We process each test case in constant time
# Space Complexity: O(1) -> No extra space used apart from a few variables
