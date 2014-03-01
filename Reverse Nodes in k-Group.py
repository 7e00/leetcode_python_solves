# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k == 0:
            return head
        myhead = ListNode(-1)
        ghead = myhead
        gtail = ghead
        cur = head
        cnt = 0
        while cur:
            ncur = cur.next
            cur.next = ghead.next
            if ghead.next == None:
                gtail = cur
            ghead.next = cur
            cur = ncur
            cnt += 1
            if cnt == k:
                cnt = 0
                ghead = gtail
        if cnt != 0:
            cur = ghead.next
            ghead.next = None
            while cur:
                ncur = cur.next
                cur.next = ghead.next
                ghead.next = cur
                cur = ncur
        return myhead.next