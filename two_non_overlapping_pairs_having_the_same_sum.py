"""
Given an UNSORTED integer array, find two non-overlapping pairs in it having the same sum of pair
"""

# Function to find two non-overlapping pairs with the same sum in a list


def find_pairs(myarr):
    # create an empty dictionary
    # key -> distinct sum a pair could have
    # value -> list, storing the index every pair having that sum
    mydict = {}

    # consider every pair (myarr[i], myarr[j]), where `j>i`
    for i in range(len(myarr)-1):
        for j in range(i+1, len(myarr)):

            # calculate the sum of current pair
            sum = myarr[i] + myarr[j]

            # check if the sum is already present in the dictionary
            if sum in mydict:

                # check every other pair in dict, having the same sum
                for pair in mydict[sum]:  # for m, n in mydict[sum_of_pair]:  # Two lines could be just 1
                    m, n = pair     # unzipping a sequence (tuple, here)

                    # check if pairs don't overlap (are non-overlapping), print them and return
                    if (m != i and n != j) and (n != i and n != j):
                        print('First Pair:', (myarr[i], myarr[j]))
                        print('Second Pair:', (myarr[m], myarr[n]))
                        return

            # We have a "return" in the previous section (if sum is already in dict condition),
            # so the control will get into this section only if the above condition is not true, i.e. sum is not
            # already present in map(dict here)

            # If the sum not already in mydict, Insert sum into the dict and map it to its pair
            # (Here, one could also write else:, or also could write the exact condition - if sum not in mydict:)
            mydict.setdefault(sum, []).append((i, j))
            print(mydict)


    print('No non-overlapping pairs present')


# Driver Code
if __name__ == "__main__":
    myarr = [3, 4, 7, 3, 4]
    myarr = [1, 7, 9, 3]
    myarr = [1, 7, 9, 3]

    find_pairs(myarr)

""" alternative to oneliner:  mydict.setdefault().append()

if sum not in mydict:
    mydict[sum] = []
mydict[sum].append((i,j))
"""

