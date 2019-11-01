#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1)
        print(l2)
        temp = ListNode(None)
        while l1 is not None and l2 is not None:
            if l1.val >= l2.val:
                temp.val = l2.val
                temp.next = l1
                l1 = temp
                l2 = l2.next
            elif l1.val < l2.val:
                temp.next = l1.next
                l1 = temp
                l1 = l1.next
            

        print(l1)
        print(l2)
        print(temp)


        
       

            

        
        

