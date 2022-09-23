"""
Given an UNSORTED integer myarray, find two non-overlapping pairs in it having the same sum_of_pair
"""

# Function to find two non-overlapping pairs with the same sum_of_pair in a list


def find_pairs(myarr):
    # create an empty dictionary
    # key -> sum_of_pair of a pair of elements in the list
    # value -> list storing an index every pair having that sum_of_pair
    mydict = {}

    # consider every pair (myarr[i], myarr[j]), where `j>i`
    for i in range(len(myarr)-1):
        for j in range(i+1, len(myarr)):
            # calculate the sum_of_pair of current pairs
            sum_of_pair = myarr[i] + myarr[j]

            # check if the sum_of_pair is already present in the dictionary
            if sum_of_pair in mydict:
                # check every pair for the desired sum_of_pair
                for m, n in mydict[sum_of_pair]:

                    # check if pairs don't overlap, print and return them
                    if (m != i and n != j) and (n != i and n != j):
                        print('First Pair:', (myarr[i], myarr[j]))
                        print('Second Pair:', (myarr[m], myarr[n]))
                        return

            # We have a "return" in the previous condition (does not overlap ) so the control will get into this section
            # only if the above conditions is not true

            # Insert current pair into the dictionary
            mydict.setdefault(sum_of_pair, []).append((i, j))

    print('No non-overlapping pairs present')


# Driver Code
if __name__ == "__main__":
    myarr = [3, 4, 7, 3, 4]
    find_pairs(myarr)





