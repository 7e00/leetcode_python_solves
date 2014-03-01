class Solution:
    def findPivot(self, A):
        l = 0
        r = len(A)-1
        while l < r:
            mid = (l+r)/2
            if A[mid] < A[0]:
                r = mid
            elif A[mid] == A[0]:
                return mid
            else:
                l = mid+1
        if A[l] < A[0]:
            return l-1
        return l
    def binaSearch(self, A, sp, ep, target):
        while sp <= ep:
            mid = (sp+ep)/2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                sp = mid+1
            else:
                ep = mid-1
        return -1
        
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        p = self.findPivot(A)
        t = self.binaSearch(A, 0, p, target)
        if t != -1:
            return t
        return self.binaSearch(A, p+1, len(A)-1, target)