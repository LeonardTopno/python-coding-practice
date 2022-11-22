"""
Given an array of integers of size ‘n’,
Our aim is to calculate the MAXIMUM sum of ‘k’ consecutive elements in the array.
Leo's Note: In subarray, the elems are in the same sequence
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
    # n must be greater than k
    if n < k:
        print("Invalid Input")
        return -1

    for i in range(n - k + 1):
        # i will be 0,1,2,... leaving the last k elem, (n-k+1), +1 becoz we will be dealing with index may be

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


