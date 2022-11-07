# Function to find minimum number of inversions needed to make the given expression balanced

def count_min_inversions(exp):

    # if the expression has an odd length, ot cannot be balaced
    if len(exp)%2:
        print("The given expression cannot be balanced")
        return -1

    inversions = 0  # stores the number of inversions needed
    open_ = 0  # stores the number of open bracket

    # traversing the expression
    for i in range(len(exp)):

        # if the current character is amn open braces, add it to the count
        if exp[i] == "{":
            open_ += 1

        # if the current Character is a closing bracket
        else:
            if open_ != 0:  # if the count of open bracket is non-zero; i.e. previous elem is an open bracket
                open_ -= 1
            else:
                open_ += 1
                inversions += 1

    return inversions + (open_//2)  # for n open braces, exactly 'n/2' inversions are needed.


# Driver Code
if __name__ == "__main__":
    # exp = "{{}{{}{{"
    exp = "}}}}"
    inv = count_min_inversions(exp)

    if inv != -1:
        print("Mini num of inversions neede is:", inv)
    else:
        print("Can't be balanced by Inversions Only")





