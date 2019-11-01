#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        
        endlist = []
        
        taa = []
        
        tda = nums.copy()
        #test = tda.pop(1)
        #print(test)
        print(nums)
        #print(tda)
        length = len(nums)

        def backtrack(array):
            for i,v in enumerate(array):
                if len(taa) != length:
                    for i, j in enumerate(tda):
                        popped = tda.pop(i)
                        print(popped)
                        print(tda)
                        taa.append(popped)
                        print(taa)
                        print("part1")
                        backtrack(taa)
                elif taa not in endlist:
                    endlist.append(taa)
                    print("gotcha")
                    taa = []
                    tda = nums.copy()
                else:
                    taa = []
                    tda = nums.copy()
        
        backtrack(nums)

        #final_list.append([3,2,1])
        
        
        
        print(endlist)

# @lc code=end

