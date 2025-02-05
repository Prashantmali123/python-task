"""Task 1.  
Find the Missing Number in an Array 
A list contains n distinct numbers taken from 0, 1, 2, ..., n, but one number is 
missing. 
Write a function to find the missing number. 
def find_missing_number(arr: list) -> int: 
pass 
Example: 
arr = [3, 0, 1] 
print(find_missing_number(arr))   Output: 2 

date : 5 feb 2025
by : prashant mali"""


def find_missing_number(arr):
    try:
        n = len(arr)
        if n == 0:
            raise ValueError("Array cannot be empty.")

        expected_sum = (n * (n + 1)) / 2
        actual_sum = sum(arr)
        missing_number = expected_sum - actual_sum
        print("Missing number is:", missing_number)

    except Exception as e:
        print("An error occurred:", e)


arr1 = []
try:
    n = int(input("Enter the value of n as array size: "))
    if n < 0:
        raise ValueError("Array size cannot be negative.")

    for i in range(n):
        try:
            j = int(input(f"Enter number {i + 1}: "))
            arr1.append(j)
        except ValueError:
            print("Invalid input! Please enter an integer.")
            break

    find_missing_number(arr1)

except ValueError as ve:
    print("Invalid input:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
