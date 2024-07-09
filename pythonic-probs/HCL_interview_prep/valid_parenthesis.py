"""
Given a string "string" containing just the characters "(", ")", "{", "}", "[", "]", determine if the input string is valid.
An inputis valid if:
    1. open brackets must be closed by same type of brackets.
    2. Open brackets must be closed in correct order  
"""

def is_valid_parenthesis(string):
    stack = [] # we initialize a stack and this will be sued to store opening brackets
    
    lookup = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    for parenthesis in string:
        if parenthesis in lookup:  #lookup.keys()
            stack.append(parenthesis)
        elif stack and parenthesis == lookup[stack[-1]]:
            stack.pop()
        else:       # stack is empty and we still have closing braces
            return False
    
    return not stack 

# Drive code
if __name__ == "__main__":
    string = "{[]}"
    print(is_valid_parenthesis(string))

"""
If the current parenthesis is an opening braces, then append it to the stack.
If the current parenthesis is a closing braces, check if we have anything if the stack and 
see if the top element at the stack is the matching opening braces of current parenthesis ()

If the current braces is a closing bracrs and there is a nothing in the stack, it means we have unpaired closing bracket. Hence not a valid parenthesis
"""


