"""
Given an array of integers of size ‘n’,
Our aim is to calculate the MAXIMUM sum of ‘k’ consecutive elements in the array.
Leo's note: In subarray (and also in substring), the elems are in the same sequence
"""
# O(n*k) solution for finding the maximum sum of the subarray of size k.
# We have NESTED LOOP, where outer loop is of O(n) and inner loop of O(k)

import sys

INT_MIN = -sys.maxsize - 1  # Global Variable, hence in CAPS


def get_max_sum(arr, k):
    """
    Returns the maximum sum in a subarray of size k
    @param arr: array
    @param k: len of subarray
    @return: int
    """
    max_sum = INT_MIN  # Initializing output result

    n = len(arr)
    # k should be smaller than n
    if k > n:
        print("Invalid Input")
        return -1

    for i in range(n - k + 1):
        # Our requirement is : We have to iterate till the point(or index) where
        # we are left with only last 'k' elems in the array.

        # i will start from 0 and then move on to 1,2,3 and so on... till a point (or index)
        # where last k elem are left in the array

        # In (n-k+1), we did +1 bcoz we are dealing with range() func, and in range(), counting beings from 0 and
        # (also the arr index beings from 0) AND range() fun does not include the 'stop' limit
        # so, did +1 so that the last elem (before the last k elem begins) is not missed out.

        curr_sum = 0
        for j in range(k):   # j will be 0,1,2,3...k-1
            curr_sum = curr_sum + arr[i+j]  # i remains const, j changes once it gets into inner loop

        max_sum = max(max_sum, curr_sum)

    return max_sum


# Driver code
if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(get_max_sum(arr, k))


"""
URL: https://www.geeksforgeeks.org/window-sliding-technique/
"""


