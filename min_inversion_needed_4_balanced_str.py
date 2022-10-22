def find_min_inversions(exp):
    if len(exp) % 2:
        print("Can't be balanced")
        return None  # return None is same as return | We can also write return -1

    unbalanced_count = 0
    for elem in exp:

        if elem == "{":
            unbalanced_count += 1
        else:
            unbalanced_count -= 1  # It could so happen that there could be more of closing braces (unbalanced), so count may become -ve, Hence we are using abs()


    return abs(
        unbalanced_count) // 2  # Python in-built func abs(x); // - int part of division result; you may also use int(abs(count)/2)

    # For n open (actually unbalanced) brackets, exactly 'n/2' inversions are needed


# Driver code
exp = "}{"
# exp = "{{{}"
# exp = "{{}{{}{{"
# exp = "{{{{{{"
# exp = "{{}{{}{{"
# exp="}}}}"
print(find_min_inversions(exp))


'''

--- 1. Thought Process
Leo's obs: The string consists of { and } only i.e. one type '{}' only, so this reduces the complexity

--- 2. Complexity Analysis
Time Complexity: O(n), where n is the len of input expression
Aux Space Complexity: 0(1), as this soln doesn't any extra space 

--- 3. Problem Tagging
Problem Type: String
Level: Medium

--- 4. Problem Attempt
Date: 23rd Aug 2021

'''
