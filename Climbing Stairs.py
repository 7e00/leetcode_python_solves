class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        return int((((1+5**0.5)/2)**(n+1) - ((1-5**0.5)/2)**(n+1))/(5**0.5))