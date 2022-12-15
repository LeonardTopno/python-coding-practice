"""
Given an array of INTEGERS of size 'n'
Our aim is to find the MAXIMUM SUM of 'k' consecutive elements in the array.
Leo's Note: subarray: the elem are in the same sequence as in the array
"""
#  O(n) solution for finding the maximum sum of the subarray of size k


def get_max_sum(arr, k):

    n = len(arr)  # get the length of the array

    # k must be smaller than n
    if k > n:
        print("Invalid Input: Subarray len should always be smaller than (or equal) to len of actual array")
        return -1

    # Initialize the window_sum to the sum of the elements of first window
    # i.e. to the sum of first k elements of the array
    window_sum = sum(arr[:k])

    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]

        max_sum = max(window_sum, max_sum)


    return max_sum  # bcz that is what we have to return


# Drive Code
if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(get_max_sum(arr,  k))
