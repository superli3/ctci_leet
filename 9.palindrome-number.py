#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        test = str(x)
        truth = True
        for i in range(len(test)//2):
            if test[i] == test[len(test)-1-i]:
                continue
            else:
                truth = False

        return truth
            
        

