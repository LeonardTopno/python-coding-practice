"""
Leetcode : 20. Valid Parenthesis
"""


def is_valid_parenthesis(exp):
    stack = []  # we initialize a stack and this will be used to store only opening braces
    lookup = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for parenthesis in exp:

        # if current parenthesis is an opening bracket
        if parenthesis in lookup:
            stack.append(parenthesis)

        # else current parenthesis is a closing bracket and stack is non-empty
        elif stack and parenthesis == lookup[stack[-1]]:  # This is better line than what is in copy
            stack.pop()

        #  curr parenthesis is a closing bracket, and stack is empty;
        #  This means we have an unmatched (extra) closing bracket. Or it may also mean,
        #  it came before next opening bracket, hence inValid.
        else:
            return False  # Not a Valid Parenthesis

    #  At end, check if stack is empty list. If empty, then Valid Parenthesis,
    return stack == []  # same as not stack: Is stack empty?


# Driver code:
if __name__ == '__main__':
    exp = '{[]}'     # s = input("Enter the string:")   ## '[]()'
    print(is_valid_parenthesis(exp))
