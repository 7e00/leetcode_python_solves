# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        llist = None
        listtail = None
        glist = None
        glisttail = None
        cur = head
        while cur:
            ncur = cur.next
            cur.next = None
            if cur.val >= x:
                if glist == None:
                    glist = glisttail = cur
                else:
                    glisttail.next = cur
                    glisttail = cur
            else:
                if llist == None:
                    llist = cur
                    listtail = cur
                else:
                    listtail.next = cur
                    listtail = cur
            cur = ncur
        if listtail:
            listtail.next = glist
        else:
            llist = glist
        return llist