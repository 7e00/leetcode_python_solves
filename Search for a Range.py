class Solution:
    def leftBinarySearch(self, A, target):
        l = 0
        r = len(A) - 1
        while l < r:
            mid = (l+r)//2
            if A[mid] >= target:
                r = mid
            else:
                l = mid+1
        if A[l] == target:
            return l
        return -1
    def rightBinarySearch(self, A, target):
        l = 0
        r = len(A) - 1
        while l < r:
            mid = (l+r+1)//2
            if A[mid] > target:
                r = mid-1
            else:
                l = mid
        if A[r] == target:
            return r
        return -1
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = self.leftBinarySearch(A, target)
        if left == -1:
            return [-1,-1]
        return [left, self.rightBinarySearch(A, target)]