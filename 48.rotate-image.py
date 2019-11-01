#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        print(matrix)
        for ri in range(n):
            for ci in range(ri, n):
                matrix[ri][ci], matrix[ci][ri] = matrix[ci][ri],  matrix[ri][ci]
        print(matrix)

        for i in matrix:
            i.reverse()

        print(matrix)
        
# @lc code=end

