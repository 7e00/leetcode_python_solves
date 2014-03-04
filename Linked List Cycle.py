# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        p1 = head
        p2 = head
        while True:
            p1 = p1.next
            p2 = p2.next
            if p2 == None:
                return False
            p2 = p2.next
            if p2 == None:
                return False
            if p1 == p2:
                break
        return True