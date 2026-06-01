# Read the number of test cases
N = int(input())

# Loop through all test cases
for i in range(N):

    # Read the number to be reversed
    Num = int(input())

    # Variable to store the reversed number
    Rev = 0

    # Process each digit of the number
    while Num > 0:

        # Extract the last digit
        Digit = Num % 10

        # Append the digit to the reversed number
        Rev = Rev * 10 + Digit

        # Remove the last digit from the original number
        Num = Num // 10

    # Print the reversed number
    print(Rev)

# Time Complexity:
# Let D be the number of digits in a number.
# The while loop runs D times.
# Therefore, for one test case: O(D)
# For N test cases: O(N × D)

# Space Complexity:
# O(1) because only a few variables (Num, Rev, Digit) are used,
# regardless of the input size.
