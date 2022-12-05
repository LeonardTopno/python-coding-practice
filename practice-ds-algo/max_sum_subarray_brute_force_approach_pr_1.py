"""
Given an array of INTEGERS of size 'n'
Our aim is to calculate the MAXIMUM sum of 'k' CONSECUTIVE elements in the array.
Leo's note: In subarray (and also in substring), the elems are in same sequence
"""
# O(n*k) solution for finding the MAXIMUM sum of the subarray of size 'k'
# We have NESTED LOOP, where the outer loop is of O(n) and inner loop is ok O(k).

import sys

INT_MIN = -sys.maxsize - 1  # GLOBAL VARIABLE, hence in caps Lock


def get_max_subarray_sum(arr, k):
    """
    Returns the maximum sum in a subarray of size k
    @param arr: array
    @param k: len of subarray
    @return: int
    """
    max_sum = INT_MIN  # Initializing max_sum which is the output result

    n = len(arr)  # k must be smaller than n
    if k > n:
        print("Invalid Input: Subarray is always smaller than (or equal) to actual array")
        return -1  # bcoz we r returning int type [Leo: FFT even sum can be -1 as it is not given that int are +ve only]

    for i in range(n-k+1):
        # We have to iterate till the point where we leave last 'k' elems of the array.
        # Did +1 so that the last elem (before the last k elem begins) is not missed out
        curr_sum = 0
        for j in range(k):
            curr_sum = curr_sum + arr[i+j]

        max_sum = max(max_sum, curr_sum)

    return max_sum


# Drive code
if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(get_max_subarray_sum(arr, k))


