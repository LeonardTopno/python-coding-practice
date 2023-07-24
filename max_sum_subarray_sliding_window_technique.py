"""
Given an array of integers of size ‘n’,
Our aim is to calculate the MAXIMUM sum of ‘k’ consecutive elements in the array.
Leo's Note: subarray: the elems are in the same sequence as in the array
"""
# O(n) solution for finding the maximum sum of the subarray of size k


def get_max_sum(arr, k):

    n = len(arr)   # get the length of the array

    # k must be smaller than n
    if k > n:
        print("Invalid Input: Subarray len should always be smaller than (or equal) to len of actual array")
        return -1

    # compute sum of first window of size k
    window_sum = sum(arr[:k])  # Pythonic one liner trick: How to compute the sum of first k elem in an array

    max_sum = window_sum  # Initializing max_sum which is the output result

    # compute the SUM of each remaining window of size k,
    # by removing the first elem of prev window and adding the last elem of curr window to the window_sum
    # And then check if it qualifies to be max_sum
    for i in range(n-k):
        # n is the length of the array, k is the length of the subarray, so (n-k) is also length
        # we did (n-k) bcz we want to traverse till a point(index) where only last 4 elem are left.
        # Leo : But why didn't we do (n-k+1) as we did in case of Brute Force Method?

        # This is bcz we are more concerned about computing window_sum,
        # (rather than in getting individual windows of size 'k' and then summing up their elem to get the curr_Sum)
        # and checking if this new window_sum qualifies to be max_sum

        # Here for COMPUTATION of window_sum (which should be our primary focus, here),
        # SUBTRACTING first elem of prev window and ADDING the next elem To window_sum, matters more.
        # In the last most errand/iteration, ADDING the last elem i.e. n-th elem (elem at n-1 index) would mean
        # SUBTRACTING the first elem of the 2nd last window => (n-k-1, n-2).
        # The fist elem to be SUBTRACTED would be the elem at index = (n-k-1).

        # Hence the max index a hind tail(pointer, here i) should achieve is n-k-1,
        # and since the range() func does not include the stop elem, for i in range(n-k) is justified as
        # in this case 'i' will attain max value as n-k-1, and that is what is needed here.


        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)

    return max_sum


# Driver code
if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(get_max_sum(arr, k))

"""
URL: https://www.geeksforgeeks.org/window-sliding-technique/
"""
