# Time Complexity: O(T)
# Space Complexity: O(1)

t = int(input())  # Number of test cases

for i in range(t):
    A = int(input())  # Read the value of A

    # Check if A is greater than or equal to 51
    if A >= 51:
        print("RIGHT")
    else:
        print("LEFT")
