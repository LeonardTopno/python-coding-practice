
#  ==========================================================
"""
Creating a key in the dictionary if it does not previously exist, and assign (append in the list, here) a value (tuple, here)
"""
if sum_of_pairs not in mydict:
    mydict[sum_of_pairs] = []  # Empty List
    mydict[sum_of_pairs].append((i, j))

# ------

mydict.setdefault(sum_of_pair, []).append((i, j))



#  ==========================================================
"""
How to compute the sum of first k elems of an arr
"""

window_sum = sum(arr[:k])

#  ==========================================================
"""
Swap the values of variables
"""

a, b = b, a

#  ==========================================================
"""
"""