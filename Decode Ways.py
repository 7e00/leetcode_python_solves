class Solution:
    def numDec(self, s, pos):
        if pos == len(s):
            return 1
        t = self.numDec(s, pos+1)
        if (pos < len(s)-1) and (s[pos] == "1" or (s[pos] == "2" and int(s[pos+1]) <= 6)):
            return t + self.numDec(s, pos+2)
        return t
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i > 1 and (s[i-2] == "1" or (s[i-2] == "2" and int(s[i-1]) <= 6)):
                dp[i] += dp[i-2]
        return dp[n]