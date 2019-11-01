#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #print("target: " + str(target))
        match = False
        #print(len(matrix))
        #print(len(matrix[0]))
        if (len(matrix) > 0):
            if (len(matrix[0]) > 0):
                newlist = []
                for i in matrix:
                    #print(i)
                    newlist = newlist + i

                #print(newlist)
            
                for i in newlist:
                    if target in newlist:
                        match = True
                    elif target < newlist[0]:
                        break
                    else:
                        continue

        return match
        

            
        

