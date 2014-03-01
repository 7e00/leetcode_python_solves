class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        t = -1
        for i in range(len(A)):
            if A[i] == target:
                t = i
                break
        return t