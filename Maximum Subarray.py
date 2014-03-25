class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        premax = A[0]
        ans = premax
        for i in range(1,len(A)):
            if A[i]+premax > A[i]:
                premax = A[i]+premax
            else:
                premax = A[i]
            ans = max(premax, ans)
        return ans