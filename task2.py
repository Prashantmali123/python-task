'''Task 2.  
Valid Parentheses Checker 
Write a function to check whether a given string containing only (), {}, [] is 
balanced. 
def is_valid(s: str) -> bool: 
pass 
Example: 
s = "{[()]}" 
print(is_valid(s))   Output: True 
s = "{[(])}" 
print(is_valid(s))   Output: False
date : 5 feb 2025
by : prashant mali'''

def is_valid(s: str) -> bool:
    try:
        if not isinstance(s, str): 
            raise ValueError("Input must be a string.")

        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}  

        for char in s:
            if char in bracket_map.values():  
                stack.append(char)
            elif char in bracket_map.keys():  
                if not stack or stack.pop() != bracket_map[char]:
                    return False 
            else:
                raise ValueError("Invalid character found! Only (), {}, [] are allowed.") 

        return len(stack) == 0  

    except ValueError as ve:
        print("Input error:", ve)
        return False
    except Exception as e:
        print("An unexpected error occurred:", e)
        return False


try:
    s = input("Enter a string with parentheses: ").strip()
    if not s:
        raise ValueError("Input cannot be empty.")
    
    
    print("Is the string valid?", is_valid(s))

except ValueError as ve:
    print("Invalid input:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
