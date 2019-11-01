#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #print(nums)
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            #print("currsum:" + str(curr_sum))
            max_sum = max(max_sum, curr_sum)
            #print("maxsum:" + str(max_sum))
            
        return max_sum
        

