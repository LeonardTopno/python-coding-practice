"""
Given an UNSORTED integer array, find two non-overlapping pairs in it having the same sum of pair
"""

# Function to find two non-overlapping pairs having the same sum in a list


def find_pairs(arr):
    # create an empty dictionary
    # keys: sum of pairs
    # values: list, storing the indices of every pair, whose total is that sum
    lookup = {}

    # consider every pair (arr[i], arr[j]), where `j>i`
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):

            # calculate the sum of current pair
            sum_ = arr[i] + arr[j]

            # check if the sum is already present in the dictionary
            if sum_ in lookup:

                # traverse through every other pair, having the same sum
                for pair in lookup[sum_]:  # for m, n in lookup[sum_]:  # Two lines could be just 1
                    m, n = pair     # unpacking pair, @type pair: tuple

                    # check if pairs don't overlap (are non-overlapping), print them and return
                    if (m != i and m != j) and (n != i and n != j):
                        print('First Pair:', (arr[i], arr[j]))
                        print('Second Pair:', (arr[m], arr[n]))
                        return

            # We have a "return" in the previous section (if sum is already in dict condition),
            # so the control will get into this section only when the above condition is not true, i.e. sum is not
            # already present in dict(lookup)

            # If the sum not already in lookup, Insert sum in the dict(lookup) and map it to its pair
            # (Here, one could also write else:, or also could write the exact condition - if sum not in lookup:)
            lookup.setdefault(sum_, []).append((i, j))  # the return value of lookup.setdefault() is as empty list, hence we can use list method append()
            print(lookup)


    print('No non-overlapping pairs with the same sum present')


# Driver Code
if __name__ == "__main__":
    arr = [3, 4, 7, 3, 4]
    # arr = [1, 7, 9, 3]
    # arr = [1, 7, 9, 3]

    find_pairs(arr)

""" alternative to oneliner:  lookup.setdefault().append()

if sum_ not in lookup:
    lookup[sum_] = []
lookup[sum_].append((i,j))
"""

