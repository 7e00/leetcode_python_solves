class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = 0
        for i in range(len(A)):
            if i == 0 or A[i] != A[i-1]:
                A[n] = A[i]
                n += 1
        return n