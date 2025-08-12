T = int(input())  # Read the number of test cases

for _ in range(T):  # Loop over each test case
    N = int(input())  # Read the number of students or items (N)

    Pages = N * 1000  # Each student/item needs 1000 pages

    Notebooks = Pages // 100  # Each notebook contains 100 pages

    print(Notebooks)  # Output the total number of notebooks needed

# Time Complexity: O(T) -> Each test case runs in constant time
# Space Complexity: O(1) -> Only a constant amount of extra memory is used
