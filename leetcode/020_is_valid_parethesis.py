def is_valid_parenthesis(exp):
    stack = []
    lookup = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for parenthesis in exp:
        if parenthesis in lookup:
            stack.append(parenthesis)
        elif stack and parenthesis == lookup[stack[-1]]:  # This is better line than what is in copy
            stack.pop()
        else:
            return False

    return stack == []  # same as not stack: Is stack empty?


# Driver code:
if __name__ == '__main__':
    exp = '{[]}'
    print(is_valid_parenthesis(exp))
