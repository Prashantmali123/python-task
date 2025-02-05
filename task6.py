'''Task 6.  
Find Kth Largest Element in an Array 
Given an unsorted list and an integer k, find the k-th largest element in the list. 
def find_kth_largest(nums: list, k: int) -> int: 
pass 
Example: 
nums = [3, 2, 1, 5, 6, 4] 
k = 2 
print(find_kth_largest(nums, k))   Output: 5 

date: 5 feb 2025
by : prashant mali'''

def find_kth_largest(nums: list, k: int) -> int:
    try:
        if not nums or k <= 0 or k > len(nums):
            raise ValueError("Invalid input: k should be between 1 and ", len(nums))
        
        nums.sort(reverse=True)  
        return nums[k - 1]  

    except Exception as e:
        print("An error occurred:", e)
        return None


nums = []
try:
    y = int(input("Enter array size: "))
    if y <= 0:
        raise ValueError("Array size must be greater than zero.")

    for i in range(y):
        while True:
            try:
                j = int(input(f"Enter number {i + 1}: "))
                nums.append(j)
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")

    k = int(input("Enter the k-th largest number: "))
    
    result = find_kth_largest(nums, k)
    if result is not None:
        print(f"The {k}-th largest element is:", result)

except ValueError as ve:
    print("Invalid input:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
