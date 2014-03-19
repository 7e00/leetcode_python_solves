# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        cur = head.next.next
        head.next.next = head
        head = head.next
        head.next.next = None
        tail = head.next
        while cur:
            ncur = cur.next
            if ncur == None:
                tail.next = cur
                break
            ncur = ncur.next
            cur.next.next = cur
            tail.next = cur.next
            tail = cur
            tail.next = None
            cur = ncur
        return head
