# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None:
            return None
        p1 = head
        p2 = head
        while True:
            p1 = p1.next
            p2 = p2.next
            if p2 == None:
                break
            p2 = p2.next
            if p2 == None:
                break
            if p1 == p2:
                break
        if p2 == None:
            return None
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p2