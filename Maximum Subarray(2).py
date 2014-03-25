class Solution:
    def maxSub(self, A, f, t):
        if f == t:
            return A[f],A[f],A[f],A[f]
        mid = (f+t)//2
        lsum,lc,ll,lr = self.maxSub(A,f,mid)
        rsum,rc,rl,rr = self.maxSub(A,mid+1,t)
        sum = lsum+rsum
        if lsum + rl >= ll:
            left = lsum+rl
        else:
            left = ll
        if rsum+lr >= rr:
            right = rsum+lr
        else:
            right = rr
        if lr+rl >= lc and lr+rl >= rc:
            center = lr+rl
        elif lc >= rc and lc >= lr+rl:
            center = lc
        else:
            center = rc
        return sum,center,left,right
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        return self.maxSub(A, 0, len(A)-1)[1]