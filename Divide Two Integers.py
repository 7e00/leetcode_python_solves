class Solution:
    def multiply(self, a, b):
        res = 0
        while b:
            if (b&1):
                res += a
            a <<= 1
            b >>= 1
        return res
    # @return an integer
    def divide(self, dividend, divisor):
        minus = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor
        k = 0
        tmp = divisor
        while tmp:
            tmp >>= 1
            k += 1
        r = dividend>>(k-1)
        l = dividend>>k
        while l <= r:
            mid = (l+r)>>1
            if dividend < self.multiply(mid, divisor):
                r = mid-1
            elif dividend - self.multiply(mid, divisor) >= divisor:
                l = mid+1
            else:
                return mid if not minus else -mid
        return l if not minus else -l