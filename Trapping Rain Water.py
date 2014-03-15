class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        res = 0
        sta = []
        top = 0
        for i in range(len(A)):
            length = 0
            while top and sta[top-1][1] <= A[i]:
                length += sta[top-1][0]
                res += (A[i]-sta[top-1][1])*sta[top-1][0]
                top -= 1
            if top == 0 and len(sta):
                res -= (A[i] - sta[0][1])*length
                length = 0
            if top == len(sta):
                sta.append((length+1,A[i]))
            else:
                sta[top] = (length+1,A[i])
            top += 1
        return res