arr = []  # Initialize an empty list to store the numbers
even = 0  # Counter for even numbers
odd = 0   # Counter for odd numbers

N = int(input())  # Read the number of elements
arr = list(map(int, input().split()))  # Read N integers into the list

for W in arr:  # Loop through each number in the list
    if W % 2 == 0:  # If the number is even
        even = even + 1  # Increment even counter
    else:  # If the number is odd
        odd = odd + 1  # Increment odd counter

if even > odd:  # If more even numbers than odd numbers
    print("READY FOR BATTLE")  # Condition satisfied
else:
    print("NOT READY")  # Condition not satisfied

# Time Complexity: O(N) -> We iterate through the list once
# Space Complexity: O(N) -> Storing the list of N integers
