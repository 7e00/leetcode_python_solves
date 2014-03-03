# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        p = head
        cur = head.next
        while cur:
            next = cur.next
            if cur.val != p.val:
                p.next = cur
                p = p.next
            cur = next
        p.next = None
        return head