"""
Approach: Linked List


1568 / 1568 test cases passed.
Status: Accepted

Runtime: 64 ms
Memory Usage: 14.1 MB

Problem link: https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(); cur = head
        p = l1; q = l2; carry = 0
        
        while p != None or q != None:
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            sum = x + y + carry
            carry = sum // 10
            cur.next = ListNode(sum%10)
            cur = cur.next
            if p != None: p = p.next
            if q != None: q = q.next
        if carry:
            cur.next = ListNode(carry)
            cur = cur.next
        return head.next
        
        