# 0527-2026 Gemini SOLUTION
# 💡 The Fix: The Stack Data Structure

# To solve this for all cases, we need a Stack (First In, Last Out). Think of it like a stack of plates in a cafeteria. You always add (push) to the top, and you always remove (pop) from the top.

#     When you see an opening bracket, you push it onto the stack.

#     When you see a closing bracket, you check the top of the stack. If it matches, you pop it off. If it doesn't match (or the stack is empty), the string is invalid.

# Here is how you can implement this cleanly in Python using a list as a stack:

def bracket_validator(in_string):
    # A map to easily match a closing bracket to its opening counterpart
    # TJS: bracket_map is a dictionary 
    #      a character is either an opening tag stored in bracket_map.values()
    #                  or closing tag stored in bracket_map.keys() [default]
    bracket_map = {")": "(", "]": "[", "}": "{"}
    
    stack = []
    # TJS: list to act as a stack
    #      when a closing tag is encounter it should match stack[-1]
    
    for c in in_string:
        # If it's an opening bracket, push it to our stack
        if c in bracket_map.values():
            stack.append(c)
            print(f"Found opening bracket: {c}")
        # If it's a closing bracket
        elif c in bracket_map:
            # If the stack is empty OR the top of the stack doesn't match, it's invalid
            if not stack or stack[-1] != bracket_map[c]:
                return False
            # Otherwise, it's a match! Pop the opening bracket off the stack
            print(f"Found match: {bracket_map[c]} matches {c} ")
            stack.pop()
            
    # If the stack is completely empty, all brackets were perfectly matched
    return len(stack) == 0

# Test Cases
print(bracket_validator("((()))"))   # True
print(bracket_validator("()()"))     # True (Your previous version failed this)
print(bracket_validator("([{}])"))   # True
print(bracket_validator("([)]"))     # False