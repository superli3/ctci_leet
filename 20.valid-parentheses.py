#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(0,len(s)):
            if s[i] in ['(','[','{']:
                open_bracket = s[i]
                continue
            if open_bracket = '(' & s[i] = ')':
                return True
            elif open_bracket = '[' & s[i] = ']':
                return True
            elif open_bracket = '{' & s[i] = '}':
                return True
            else:
                return False
        print(test)

