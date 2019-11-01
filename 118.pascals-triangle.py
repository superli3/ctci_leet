#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        print(numRows)
        if numRows == 0:
            return []
        elif numRows == 1: 
            return [[1]]
        else:
            master_list = [[1]]
            cur_list = [1]

            for i in range(numRows-1):
                len_cur_list = len(cur_list)
                temp_cur_list = []
                for j in range(len_cur_list+1):
                    if j == 0 or j == len_cur_list:
                        val = 1
                    else:
                        val = cur_list[j-1] + cur_list[j]
                    temp_cur_list.append(val)
                print(cur_list)
                master_list.append(temp_cur_list)
                cur_list = temp_cur_list
            print(master_list)
            return(master_list)
# @lc code=end

