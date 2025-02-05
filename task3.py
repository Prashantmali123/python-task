'''Task 3.  
Find the First Non-Repeating Character 
Given a string, return the first non-repeating character. If all characters repeat, return 
"None". 
def first_unique_char(s: str) -> str: 
pass 
Example: 
s = "swiss" 
print(first_unique_char(s))   Output: "w" 
date : 5 feb 2025
by : prashant mali'''

def first_unique_char(s: str) -> str:
    try:
        if not s:
            return "None" 
        
        char_count = {} 
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for char in s:
            if char_count[char] == 1:
                return char
        return "None"  

    except Exception as e:
        return f"An error occurred: {e}"

s = input("Enter a string: ").strip()
print("First non-repeating character:", first_unique_char(s))
