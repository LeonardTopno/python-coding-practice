"""
Given an array of INTEGERS of size 'n'
Our aim is to calculate the MAXIMUM sum of 'k' CONSECUTIVE elements in the array.
Leo's note: In subarray (and also in substring), the elems are in same sequence
"""
# O(n) solution for finding the minimum sum of the subarray of size k


def get_max_subarray_sum(arr, k):
    n = len(arr)  # get the len of the array

    # k (len of the subarray) must be smaller (or equal to) than the len of the arr

    if k > n:
        print("Invalid Input: Subarray is always smaller than (or equal) to actual array")
        return -1  # bcz we r returning int type [Leo: FfT even sum can be -1 as it is not given that int are +ve only]

    # compute sum of first window of size k
    window_sum = sum(arr[:k])  # Pythonic one liner trick: How to compute the sum of first k elem in an array

    max_sum = window_sum  # Initializing max_sum which is the output result

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)

    return max_sum


# Driver code
if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(get_max_subarray_sum(arr, k))
