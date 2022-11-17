# Python program to implementing prefix aum array
"""
To fill the prefix sum array, we run through index 1 to last and keep on  adding the present element with previous
value in the prefix sum array.
Below is the implementation:
"""

def fill_prefix_sum(arr_, n, prefix_sum):

    prefix_sum[0] = arr_[0]

    # adding present element with the previous element

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1]+arr_[i]


# Driver Code
if __name__ == "__main__":
    arr = [10, 4, 16, 20]
    n = len(arr)

    prefixSum = [0 for i in range(n+1)]
    print(prefixSum)

    fill_prefix_sum(arr, n, prefixSum)

    for i in range(n):
        print(prefixSum[i], " ", end="")

"""
https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/

The elements of prefix sum will always be increasing in value.
"""