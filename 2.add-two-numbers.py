#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = pointer = ListNode(None)
        carry_me = 0

        cur_l1 = l1
        cur_l2 = l2

        while cur_l1 is not None and cur_l2 is not None:

            if cur_l1.val + cur_l2.val < 10:
                pointer.val = cur_l1.val + cur_l2.val + carry_me
                carry_me = 0
            else:
                carry_me = (cur_l1.val + cur_l2.val) // 10
                pointer.val = (cur_l1.val + cur_l2.val) % 10

            if cur_l1.next is not None and cur_l2.next is not None:
                pointer.next = ListNode(None)
                pointer = pointer.next
                cur_l1 = cur_l1.next
                cur_l2 = cur_l2.next
            elif carry_me > 0:
                pointer.next = ListNode(None)
                pointer.next.val = 1
                cur_l1 = cur_l1.next
                cur_l2 = cur_l2.next
            else:
                pointer.next = None
                cur_l1 = cur_l1.next
                cur_l2 = cur_l2.next

        while cur_l1 is not None:
            if cur_l1.val + carry_me < 10:
                pointer.val = cur_l1.val + carry_me
                carry_me = 0
            else:
                carry_me = (cur_l1.val + carry_me) // 10
                pointer.val = (cur_l1.val + carry_me) % 10
            
            if cur_l1.next is not None:
                pointer.next = ListNode(None)
                pointer = pointer.next
                cur_l1 = cur_l1.next
            else:
                pointer.next = None
                cur_l1 = cur_l1.next

        while cur_l2 is not None:
            if cur_l2.val + carry_me < 10:
                pointer.val = cur_l2.val + carry_me
                carry_me = 0
            else:
                carry_me = (cur_l2.val + carry_me) // 10
                pointer.val = (cur_l2.val + carry_me) % 10
            
            if cur_l2.next is not None:
                pointer.next = ListNode(None)
                pointer = pointer.next
                cur_l2 = cur_l2.next
            else:
                pointer.next = None
                cur_l2 = cur_l2.next


        return head

        

