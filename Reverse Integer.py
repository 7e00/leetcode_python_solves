class Solution:
    # @return an integer
    def reverse(self, x):
        res = 0
        minus = (x < 0)
        if minus: x = -x
        while x:
            res = res*10 + x%10
            x /= 10
        if minus:
            res = -res
        return res