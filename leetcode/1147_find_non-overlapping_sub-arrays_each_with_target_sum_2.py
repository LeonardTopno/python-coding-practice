# HashMap and
import itertools
import math


def find_min_sum_of_len_of_2_sub_arr_with_target_sum(arr, target):

    prefix = {0: -1}
    best_till = [math.inf] * len(arr)

    ans = best = math.inf

    '''
    min_sum_of_len = 999999  # to store the sum of length of sub-arrays
    best = [999999]*len(arr)  # best is a list
    prefix = 0
    latest = {0: -1}
    '''

    for index, curr in enumerate(itertools.accumulate(arr)):

        if (curr - target) in prefix:
            end = prefix[curr-target]  # Took Value of a key from the dict latest

            if end > -1:
                ans = min(ans, index-end + best_till[end])

            best = min(best, index-end)

        best_till[index] = best
        prefix[curr] = index


    return -1 if ans == math.inf else ans


if __name__ == "__main__":
    arr = [5, 2, 6, 3, 2, 5]
    target = 5
    print(find_min_sum_of_len_of_2_sub_arr_with_target_sum(arr, target))



"""
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/solutions/685470/python-one-pass-prefix-sum-o-n/
"""