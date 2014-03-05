# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        c = 0
        head = ListNode(0)
        p3 = head
        while p1 and p2:
            v = p1.val+p2.val+c
            p3.next = ListNode(v%10)
            c = v/10
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        while p1:
            v = p1.val + c
            p3.next = ListNode(v%10)
            c = v/10
            p1 = p1.next
            p3 = p3.next
        while p2:
            v = p2.val + c
            p3.next = ListNode(v%10)
            c = v/10
            p2 = p2.next
            p3 = p3.next
        if c:
            p3.next = ListNode(c)
        return head.next