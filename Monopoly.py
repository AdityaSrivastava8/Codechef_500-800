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

#Second Method
# Loop for each test case
for i in range(int(input())):
    c = 0  # Flag to check if condition is satisfied
    a = list(map(int, input().split()))  # Read list of 4 integers

    # Iterate over each number in the list
    for j in a:
        # If any number is greater than the sum of the rest
        if j > (sum(a) - j):
            c = 1  # Condition satisfied
            break  # Exit loop early

    # Print result based on condition
    if c == 1:
        print("yes")
    else:
        print("no")

# Time Complexity: O(T * n) → for T test cases, sum(a) is O(n), repeated for n numbers
# Space Complexity: O(n) → storing the list of numbers 

#Third Method 
# Read number of test cases
t = int(input())  

# Loop over test cases
for i in range(t):
    l = list(map(int, input().split()))  # Read list of 4 integers
    l.sort()  # Sort the list in ascending order

    lar = l.pop()  # pop() removes and returns the last element (largest after sorting)

    # If the largest element is greater than the sum of the remaining
    if sum(l) < lar:
        print("yes")
    else:
        print("no")

# Time Complexity: O(T * n log n) → sorting takes O(n log n) per test case
# Space Complexity: O(n) → storing the list of numbers

