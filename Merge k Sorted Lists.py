# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node != None:
                heapq.heappush(heap, (node.val, node))
        head = ListNode(-9999999999)
        tail = head
        while True:
            if len(heap) == 0:
                break
            tail.next = heapq.heappop(heap)[1]
            tail = tail.next
            if tail.next != None:
                heapq.heappush(heap, (tail.next.val, tail.next))
        
        return head.next