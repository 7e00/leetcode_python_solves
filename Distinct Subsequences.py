class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        n = len(S)
        m = len(T)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if j > i:
                    break
                dp[i][j] = dp[i-1][j]
                if S[i-1] == T[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[n][m]