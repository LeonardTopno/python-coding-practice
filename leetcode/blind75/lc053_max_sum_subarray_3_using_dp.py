import sys
class Solution(object):

    def get_max_sum_subarray(self, arr):
        @cache
        def solve(index_, must_pick):
            if index_ >= len(arr): return 0 if must_pick else -sys.maxsize    

            return max(arr[index_] + solve(index_ + 1, True), 0 if must_pick else solve(index_ + 1, False)) 
        return solve(0, False)         
