# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None
        p2 = head
        for i in range(n):
            p2 = p2.next
        pp1 = None
        p1 = head
        while p2:
            pp1 = p1
            p1 = p1.next
            p2 = p2.next
        if pp1 == None:
            return p1.next
        pp1.next = p1.next
        return head