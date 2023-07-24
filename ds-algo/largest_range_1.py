class Solution:

    # noinspection PyMethodMayBeStatic
    # Above line is only for pyCharm Warning Message
    def get_largest_range(self, nums):
        longest_range = 0
        num_set = set(nums)

        print(nums)
        print(num_set)  # set arranged the numbers in increasing order (Something new for LEO)

        final_left_val = final_right_val = 0

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
                    left_value = num
                    current_num += 1
                    current_range += 1
                    right_val = current_num

                longest_range = max(longest_range, current_range)
                if (right_val - left_value) >= (final_right_val-final_left_val):
                    final_right_val = right_val
                    final_left_val = left_value
        return longest_range, final_left_val, final_right_val


if __name__ == "__main__":
    arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    print(Solution().get_largest_range(arr))
    

""""
SOl: https://leetcode.com/problems/longest-consecutive-sequence/solutions/127576/official-solution/

Note: 
The solution is official solution but Leo needs to comment it and make it his own style 


"""