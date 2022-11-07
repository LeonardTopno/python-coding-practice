# Function to find minimum number of inversions needed to make the given expression balanced

def count_min_inversions(exp):

    # if the expression has an odd length, it cannot be balanced
    if len(exp) % 2:
        return -1

    inversions = 0  # stores all inversions needed
    open_ = 0  # stores number of opening braces

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

            # when there are no open braces found currently, convert the current brace } to {,
            # increment inversions by 1 and open_ by 1
            else:
                inversions += 1

                open_ += 1  # Leo: I guess it can also be open_ += 1 (it can just be open_ = 1
                # because it is 0 atm (0+1=0))

    # for `n` opened braces, exactly `n/2` inversions are needed
    return inversions + (open_ // 2)


# Driver Code
if __name__ == "__main__":
    # exp = "{{{}"
    # exp = "{{}{{}{{"
    # exp = "{{{{{{"
    # exp = "{{}{{}{{"
    # exp="}}}}"
    exp = "}}}}"
    inv = count_min_inversions(exp)

    if inv != -1:
        print("Minimum num of inversions needed is", inv)
    else:
        print("Can't be balanced by Inversions Only")


'''

--- 1. Thought Process
Leo's obs: The string consists of { and } only i.e. one type '{}' only, so this reduces the complexity


The idea is to traverse the given expression and maintain a count of open braces in the expression seen.
    i) If the current character is an opening brace {, increment the opening brace count by 1.
    ii) If the current character is a closing brace }, check if it has an unclosed brace to its left (look for 
        on zeo opened brace count)
        a) If any unclosed brace is found, close it using current brace and decrement the count of opened 
        b) Otherwise, convert the current brace } to { and increment the total inversions needed by 1
        and also increment the opening brace count by 1.
    iii) After we are done processing each character in the expression, if there are 'n' opened braces, we need exactly 
        n/2 inversions to close them 

--- 2. Complexity Analysis
Time Complexity: O(n), where n is the length of input expression
Aux Space Complexity: 0(1), as this soln doesn't any extra space 
- url : https://www.techiedelight.com/minimum-number-inversions-expression-balanced/

--- 3. Problem Tagging
Problem Type: String
Level: Medium

--- 4. Problem Attempt
Date: 23rd Aug 2021

'''