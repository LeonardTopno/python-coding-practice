import sys
class Solution(object):
    
    def maxSubArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_sum = (-sys.maxsize) - 1  # Whatever you have to return, initialize that. Since we are asked to return max_sum, we should initialize it to minimum possible integer

        for i in range(len(arr)): # it should not be (len(arr) -1) as it will fail in case the arr size is 1 
            curr_sum = 0
            for j in range(i, len(arr)):
                curr_sum += arr[j]

                max_sum = max(max_sum, curr_sum)

        return max_sum
    
    # Driver code
if __name__ == "__main__":
    solution = Solution()
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum = solution.maxSubArray(arr)
    print("Max sum:", max_sum)
