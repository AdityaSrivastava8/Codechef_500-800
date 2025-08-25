# Read the number of test cases
T = int(input())  

# Loop over all test cases
for character in range(T):  
    # Read four integers P, Q, R, S
    P, Q, R, S = map(int, input().split())  

    # Check if any one number is greater than the sum of the other three
    # If true, print "YES", else "NO"
    if (P + Q + R) < S or (P + Q + S) < R or (P + R + S) < Q or (Q + R + S) < P:  
        print("YES")  
    else:  
        print("NO")  

# Time Complexity: O(T) → each test case requires constant time checks
# Space Complexity: O(1) → only a fixed number of variables are used
