class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int] 
        """
        look_up = {}    # elem-> index # The things we are looking for(here index) should be value and not key 

        for index, elem in enumerate(nums):
            if target-elem in look_up:
                return[look_up[target-elem],index]
            else:
                look_up[elem]=index

        return[]

if __name__=="__main__":
    nums = [2,7,11,15] 
    target = 9

    sol_obj = Solution()
    print(sol_obj.twoSum(nums, target))