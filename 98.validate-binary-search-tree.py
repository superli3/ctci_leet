#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        print(root.val)
        print(root.left.val)
        print(root.right.val)
        if root.left.val < root.right.val:
            print("yes")
        




