T = int(input())  # Read number of test cases. O(1)  
for i in range(T):  # Loop through all test cases. O(T)  
    X, Y = map(int, input().split())  # Read two integers X and Y. O(1)  
    if X > Y:  # Compare if X is greater than Y. O(1)  
        print("Car")  # Output "Car". O(1)  
    elif X < Y:  # Compare if X is less than Y. O(1)  
        print("Bike")  # Output "Bike". O(1)  
    else:  # Case when X equals Y. O(1)  
        print("Same")  # Output "Same". O(1)  

# Time Complexity: O(T) — Each test case is processed in constant time.  
# Space Complexity: O(1) — No extra space used apart from variables.  
