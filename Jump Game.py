class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) == 0:
            return True
        nowMax = 0
        for i in range(0, len(A)):
            if i <= nowMax:
                nowMax = max(nowMax, i+A[i])
            if nowMax >= len(A)-1:
                break
        return nowMax >= len(A)-1