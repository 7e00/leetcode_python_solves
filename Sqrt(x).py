class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        l = 1
        r = x
        while l < r:
            mid = (l+r+1)>>1
            if mid*mid > x:
                r = mid-1
            else:
                l = mid
        return l