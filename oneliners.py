
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



#  ==========================================================
"""
How to fill in arr1 from index m onnwards with elements of arr2, (irrespective of whether index m is there or not in arr1)
"""
arr1[m:] = arr2  # Leo: Py Pro Tip - Everything in arr1 from index-m (not size m; moreover for list of size m, index starts from 0 and ends at m-1) onwards will be the elements of arr2
    # Leo: This can be added in python one liner. The is like append funtion of List. Ignore whatever is there (or not there) from index m onwards and append the all the elems of arr2, irrespective of size of arr1
    print(arr1)
    