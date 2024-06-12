import sys

class Solution(object):

    def maxSubArray(self, arr):
        """
        :type arr: List[int]
        :rtype: (int, List[int])
        """
        max_sum = (-sys.maxsize) - 1 
        max_sum_subarray_start_index = 0
        max_sum_subarray_end_index = 0

        for i in range(len(arr)):  # it should not be (len(arr) - 1) as it will fail in case the arr size is 1 
            curr_sum = 0
            for j in range(i, len(arr)):
                curr_sum += arr[j]

                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_sum_subarray_start_index = i
                    max_sum_subarray_end_index = j

        return max_sum, arr[max_sum_subarray_start_index:max_sum_subarray_end_index+1]

# Driver code
if __name__ == "__main__":
    solution = Solution()
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum, subarray = solution.maxSubArray(arr)
    print("Max sum:", max_sum)
    print("Subarray with max sum:", subarray)
