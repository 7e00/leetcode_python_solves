class Solution:
    def findKNum(self, A, sa, ea, B, sb, eb, k):
        if sa > ea:
            return B[sb+k-1]
        if sb > eb:
            return A[sa+k-1]
        pa = (sa+ea)/2
        mA = A[pa]
        pb = (sb+eb)/2
        mB = B[pb]
        if mA < mB:
            if k<= pa-sa+1:
                return self.findKNum(A,sa,pa,B,sb,pb-1,k)
            elif k <= pb-sb+1+pa-sa+1:
                if sb == pb:
                    return self.findKNum(A,pa+1,ea,B,sb,pb,k-pa+sa-1)
                return self.findKNum(A, sa, ea, B, sb, pb, k)
            else:
                return self.findKNum(A, pa+1, ea, B, sb, eb, k-pa+sa-1)
        elif mA == mB:
            if k < pa-sa+1+pb-sb+1:
                return self.findKNum(A,sa,pa-1,B,sb,pb-1,k)
            elif k == pa-sa+1+pb-sb+1:
                return mA
            else:
                return self.findKNum(A,pa+1,ea,B,pb+1,eb,k-pa+sa-1-pb+sb-1)
        else:
            if k <= pb-sb+1:
                return self.findKNum(A,sa,pa-1,B,sb,pb,k)
            elif k <= pa-sa+1+pb-sb+1:
                if sa == pa:
                    return self.findKNum(A,sa,pa,B,pb+1,eb,k-pb+sb-1)
                return self.findKNum(A,sa,pa,B,sb,eb,k)
            else:
                return self.findKNum(A, sa, ea, B, pb+1, eb, k-pb+sb-1)
    def findKNum2(self,A,sa,ea,B,sb,eb,k):
        if ea-sa > eb-sb:
            return self.findKNum2(B,sb,eb,A,sa,ea,k)
        if sa > ea:
            return B[sb+k-1]
        if sb > eb:
            return A[sa+k-1]
        if k == 1:
            return min(A[sa], B[sb])
        pa = min(k/2,ea-sa+1)
        pb = k-pa
        if A[sa+pa-1] < B[sb+pb-1]:
            return self.findKNum2(A, sa+pa, ea, B, sb, eb, k-pa)
        elif A[sa+pa-1] > B[sb+pb-1]:
            return self.findKNum2(A, sa, ea, B, sb+pb, eb, k-pb)
        else:
            return A[sa+pa-1]
    # @return a float
    def findMedianSortedArrays(self, A, B):
        tn = len(A)+len(B)
        if tn%2 == 1:
            return self.findKNum2(A,0,len(A)-1, B, 0,len(B)-1, (tn+1)/2)
        return (self.findKNum2(A,0,len(A)-1,B,0,len(B)-1,tn/2) + self.findKNum2(A,0,len(A)-1,B,0,len(B)-1,tn/2+1))/2.0