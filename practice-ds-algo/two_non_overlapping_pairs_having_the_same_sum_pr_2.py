"""
Date: 2024-04-19
Given an UNSORTED integer Array, find TWO (only two, return after two) non-overlapping pairs in it having the same pair
of sum.
"""
# Function to find two non-overlapping pairs having the same sum in a list


def find_pairs(arr):
    # i) create a dictionary
    # keys: sum of pairs
    # values: list, storing indices of pairs (in tuple), whose total is the key

    lookup = {}

    # ii) consider every possible pair (arr[i], arr[j]) where ``````` j>i
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):

            # iii) calculate the  sum of pairs
            sum_ = arr[i] + arr[j]

            # iv) check if the sum is already present in the lookup(dictionary)
            if sum_ in lookup:
                # traverse through every other pair in the value section of the dictionary
                # and check if they are overlapping

                for pair in lookup[sum_]:
                    m, n = pair  # unpack the tuple

                    # checking if the two pairs are non-overlapping
                    if (m!=i and m!=j) and (n!=i and n!=j):
                        # found the non-overlapping pair, hence print them
                        print("First pair: ", (arr[i], arr[j]))
                        print("Second pair: ", (arr[m], arr[n]))
                        return

            # else part: if sum_ is not already in the dictionary
            lookup.setdefault(sum_, []).append((i, j))  # appending a tuple

    print("No non-overlapping pairs with the same sum")
