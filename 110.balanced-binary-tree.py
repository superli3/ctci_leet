#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        try:
            def return_height(branch):
                if branch.left is None and branch.right is None:
                    height = 0
                else:
                    height = max(return_height(branch.left), return_height(branch.right))
                #print(height)
                height = height + 1
                #print(height)
                return height
            if abs(return_height(root.left) - return_height(root.right)) <= 1:
                return True
            else:
                return False
        except:
            return False
            

