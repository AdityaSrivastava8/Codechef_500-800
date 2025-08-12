for _ in range(int(input())):  # Loop over the given number of test cases
    x, y = map(int, input().split())  # Read two integers x and y

    print((x * y) // 100)  # Calculate (x * y) divided by 100 using integer division

# Time Complexity: O(T) -> Each test case runs in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
