T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    A, B, C, D = map(int, input().split())  # Read four integers A, B, C, D

    E = A + B + C + D  # Calculate the sum of the four integers

    if E == 0:  # If the sum is exactly zero
        print("IN")  # Condition satisfied: print "IN"
    else:
        print("OUT")  # Condition not satisfied: print "OUT"

# Time Complexity: O(T) -> Each test case runs in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
