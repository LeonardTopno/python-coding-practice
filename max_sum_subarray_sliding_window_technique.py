"""
Given an array of integers of size ‘n’,
Our aim is to calculate the MAXIMUM sum of ‘k’ consecutive elements in the array.
Leo's Note: subarray: the elems are in the same sequence
"""
# O(n) solution for finding the maximum sum of the subarray of size k


def get_max_sum(arr, k):

    # length of the subarray
    n = len(arr)

    # n must be greater than k
    if n < k:
        print("Invalid Input")
        return -1

    # compute sum of first window of size k
    window_sum = sum(arr[:k])

    max_sum = window_sum

    # compute the sum of remaining window, by removing the first elem of prev window and adding the last elem of curr
    # window
    for i in range(n-k):
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
