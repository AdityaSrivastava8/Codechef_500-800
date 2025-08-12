T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    N = int(input())  # Read the input value N

    # Calculation: base total
    Total = 50 * N  

    # Calculate expenses: 20% + 20% + 30% of Total
    X = (Total * 20) // 100 + (Total * 20) // 100 + (Total * 30) // 100  

    # Remaining amount after expenses
    Y = Total - X  

    print(Y)  # Output the remaining amount

# Time Complexity: O(T) -> Each test case runs in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used

