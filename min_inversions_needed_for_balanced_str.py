# Function to find minimum number of inversions needed to make the given expression balanced

def count_min_inversions(exp):

    # if the express has an odd length, it cannot be balanced
    if len(exp)%2:
        print("The given expression can be balanced")
        return

    inversions = 0  # stores all inversions needed
    open_ = 0  # stores total number of opening braces

    # traversing the expression
    for i in range(len(exp)):

        # if the current character is an opening brace, add it to the count
        if exp[i] == "{":
            open_ += 1

        # if the current character is a closing brace,
        else:
            # if an opening brace is found before, close it
            if open_:  # if the count of open braces is non-zero, i.e. previous elem is an open brace
                open_ -= 1

            else:     # when there are no open braces unattended currently
                inversions += 1

                open_ += 1  # Leo: I guess it can also be open_ += 1

    # for `n` opened braces, exactly `n/2` inversions are needed
    return inversions + (open_//2)


# Driver Code
if __name__ == "__main__":
    # exp = "}{"
    # exp = "{{}{{}{{"
    exp = "{{{}"
    # exp = "{{}{{}{{"
    # exp = "{{{{{{"
    # exp = "{{}{{}{{"
    # exp = "}}}}"
    inv = count_min_inversions(exp)

    if inv != -1:
        print("Minimum num of inversions needed is", inv)
    else:
        print("Can't be balanced by Inversions Only")

"""
--- 2. Complexity Analysis
Time Complexity: O(n), where n is the len of input expression
Aux Space Complexity: 0(1), as this soln doesn't any extra space

- url : https://www.techiedelight.com/minimum-number-inversions-expression-balanced/
"""