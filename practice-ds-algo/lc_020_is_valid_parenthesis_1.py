def is_valid_parenthesis(exp):
    stack = []  # initializing a stack (actually a pythonic list) to store only the opening bracket
    look_up = {
        '{': '}',
        '[': ']',
        '(': ')',
    }

    for parenthesis in exp:
        # if the parenthesis is an open bracket, store it in stack
        if parenthesis in look_up.keys():
            stack.append(parenthesis)

        # if parenthesis is a close bracket, check if the prev parenthesis is an open bracket
        elif stack and parenthesis == look_up[                  stack[-1]]:
            stack.pop()

        else:
            return False

    return stack == [] # same as not stack: Is stack empty


# Driver Code
if __name__ == "__main__":
    exp = "{[()]}"
    print(is_valid_parenthesis(exp))