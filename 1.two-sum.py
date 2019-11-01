#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        capture = []
        for index, value in enumerate(nums):
            for i in range(index, len(nums)):
                second = nums[i]
                if (value + second == target) & (index != i):
                    #print(value + nums[i])
                    capture = [index, i]
                else:
                    continue
        return capture
