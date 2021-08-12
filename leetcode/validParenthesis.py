#Leetcode : 20. Valid Parenthesis
def isValidParenthesis(s):
    
    stack = [] # we initialize a stack and this will be used to store only opening braces 
    
    lookup = {
        '(':')',
        '[':']',
        '{':'}'
    }

    for parenthesis in s:

        # if current parenthis is an opening bracket
        if parenthesis in lookup:                                       # in lookup -> looks for key; in lookup.value --> looks for value  
            stack.append(parenthesis)
        
        #current parenthesis is a closing bracket and stack is non-empty
        elif stack and lookup[stack[-1]] == parenthesis:
            stack.pop()
        
        #curr parenthesis is a closing bracket, and stack is empty; This means we have an unmatched (extra) closing bracket. Or it may also mean, it came before next opening bracket, hence inValid.
        else:
            return False  # Not a Valid Parenthesis
        

    '''Finally when we have gone through our entire loop, our stack should be empty in case of Valid Parenthesis'''
    return stack == [] # At end, check if stack is empty list. If empty, then Valid Parenthis, we got matching opening brances for all closing braces found

# Drive Code
if __name__ == '__main__':
    s = '[]()'              # s = input("Enter the string:")
    print(isValidParenthesis(s))


