class Solution:

    # noinspection PyMethodMayBeStatic
    # Above line is only for pyCharm Warning Message
    def get_largest_range(self, nums):
        longest_range = 0
        num_set = set(nums)

        print(nums)
        print(num_set)  # set arranged the numbers in increasing order (Something new for LEO)

        """
        We will start from a element and see how far can we go, while maintaining the 
        """
        for num in num_set:
            if num - 1 not in num_set:  # if prev num there then we will move to next elem in the num_set
                # till we get a num for which prev_num is not there in the num_set,
                # no need to get into loop and the following steps if prev_num is there
                current_num = num
                current_range = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_range += 1

                longest_range = max(longest_range, current_range)

        return longest_range


if __name__ == "__main__":
    arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    print(Solution().get_largest_range(arr))
    

""""
SOl: https://leetcode.com/problems/longest-consecutive-sequence/solutions/127576/official-solution/

Note: 
The solution is official solution but Leo needs to comment it and make it his own style 

Intuition: 
    It turns out that our initial brute force solution was on the right track, but missing a few optimization 
    necessary to reach O(n) Time Complexity

Algorithm:
    The optimized algorithm contains only two changes from the brute force approach:
    i) The numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups, 
    ii) and we only attempt to build sequences from numbers that are not already a part of longer sequence 
        This is accomplished by first ensuring that the number that would immediately preceed the current number is a 
        sequence is not present, as that number would necessarily be part of a longer sequence.
"""