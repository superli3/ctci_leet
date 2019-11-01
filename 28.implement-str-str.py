#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        value = -1
        if (len(haystack) > 0) & (len(needle) > 0) & (len(needle) < len(haystack)):
            for i, v in enumerate(haystack):
                if needle == haystack[i:i+len(needle)]:
                    value = i
                    #print(value)
                    print(i)
                    #print(v)
                else:
                    continue
        else:
            pass
        return value

