import sys

class Solution(object):

    def maxSubArray(self, arr):
        """
        :type arr: List[int]
        :rtype: (int, List[int])
        """
        max_sum = (-sys.maxsize) - 1 
        subarray_start_index = 0
        subarray_end_index = 0

        for i in range(len(arr)):  # it should not be (len(arr) - 1) as it will fail in case the arr size is 1 
            curr_sum = 0
            for j in range(i, len(arr)):
                curr_sum += arr[j]

                if curr_sum > max_sum:
                    max_sum = curr_sum
                    subarray_start_index = i
                    subarray_end_index = j

        return max_sum, arr[subarray_start_index:subarray_end_index+1]

# Driver code
if __name__ == "__main__":
    solution = Solution()
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum, subarray = solution.maxSubArray(arr)
    print("Max sum:", max_sum)
    print("Subarray with max sum:", subarray)



""""
NOT FAIRED
Time Complexity: O(n) where n is the length of the array
    Reason: Iterating through the array takes O(n)
            The elems are stored in a hash map (or dictionary, in Python) which allows O(1) lookups.
            So O(n) + O(1) = (n)
NOT FAIRED
Space Complexity: O(n)
    Reason: An additional Data Structure has been introduced - dictionary, which can at max contain n elements (if no duplucates found)


Note(If Any): 

NOT FAIRED
Intuition: Dictionary can not contain duplicate keys. 
            So use a dictionary (hash-map) to store encountered elements. 
            While iterating through the arr, check if the elem is alreay in the dict.
            If yes: We have found a duplicate, hence return True.
            If no: Add the elem to the dictionary. syntax: my_dict.get(key, default_key)
            
            Mantra:  In a Hash Map (Pythonic Dictionary), the keys are suppose to be unique.  
        

Algorithm: 

FAIRED
Sol URL: https://leetcode.com/problems/maximum-subarray/solutions/1595195/c-python-7-simple-solutions-w-explanation-brute-force-dp-kadane-divide-conquer/

""" 