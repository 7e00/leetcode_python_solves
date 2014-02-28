class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        num = 0
        n = len(A)
        i = 0
        while i+num < n:
            while i + num < n and A[i] == elem:
                A[i] = A[n-num-1]
                num += 1
            i += 1
        return n-num