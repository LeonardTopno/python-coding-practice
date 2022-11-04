"""
Given an UNSORTED integer array, find TWO (only two, return after you find two) non-overlapping pairs in it having
the same sum pf pair
"""


#  Function to find two non-overlapping pairs having the same sum in a list
def find_pairs(arr):
    # create an array
    # keys: sum of pairs
    # values: list, storing indices of pair, whose total is that sum
    lookup = {}

    # consider every possible pair (arr[i], arr[j]) where `j>i`

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):

            #  calculate the sum of pairs
            sum_ = arr[i]+arr[j]

            # check if this sum_ is already as key in the lookup (dictionary)
            if sum_ in lookup:

                # traverse through every other pair having the same sum
                for pair in lookup[sum_]:
                    m, n = pair  # unpacking pair, @type pair:tuple

                    # check if the two pairs in hand do not overlap
                    if (m != i and m != j) and (n != i and n != j):
                        print('First Pair:', (arr[i], arr[j]))
                        print('Second Pair:', (arr[m], arr[n]))
                        return

            # if sum_ is not already in lookup
            lookup.setdefault(sum_, []).append((i, j))

    print("No non-overlapping pairs with same sum present")


# Driver Code
if __name__ == "__main__":
    arr = [1, 7, 9, 3]
    arr = [3, 4, 7, 3, 4]
    find_pairs(arr)
