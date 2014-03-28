# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None:
            return None
        if k == 0:
            return head
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            if cnt > k:
                break
            cur = cur.next
        else:
            k %= cnt
            cur = head
            for i in range(k):
                cur = cur.next
        if k == 0:
            return head
        pcur = head
        while cur.next:
            cur = cur.next
            pcur = pcur.next
        newhead = pcur.next
        pcur.next = None
        cur.next = head
        return newhead