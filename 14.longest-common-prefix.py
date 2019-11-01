#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs,key=len)
        
        for i in range(len(shortest_string)):
            #loop through list
            for j in strs:
                if shortest_string = j[0:len(shortest_string)]:
                    
                shortest_string = shortest_string[0:len(shortest_string)-1]
                print(shortest_string)
        

