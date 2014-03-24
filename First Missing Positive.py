class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = 0
        i = 0
        while i < len(A)-n:
            if A[i] <= 0:
                A[i] = A[len(A)-n-1]
                n += 1
                continue
            if A[i] > len(A) - n:
                A[i] = A[len(A)-n-1]
                n += 1
                continue
            if A[A[i]-1] == A[i]:
                i += 1
                continue
            if A[i]-1 <= i:
                A[A[i]-1] = A[i]
                i += 1
            else:
                tmp = A[A[i]-1]
                A[A[i]-1] = A[i]
                A[i] = tmp
        for i in range(len(A)-n):
            if A[i] != i+1:
                return i+1
        else:
            return len(A)-n+1