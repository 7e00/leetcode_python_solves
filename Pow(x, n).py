class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        res = 1
        k = n if n >= 0 else -n
        while k:
            if k&1:
                res *= x
            x *= x
            k >>= 1
        return res if n > 0 else 1.0/res