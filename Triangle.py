class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        dp = [[999999999 for i in range(len(triangle))] for j in range(2)]
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            dp[i&1][0] = dp[1-(i&1)][0] + triangle[i][0]
            for j in range(1, i):
                dp[i&1][j] = min(dp[1-(i&1)][j-1], dp[1-(i&1)][j]) + triangle[i][j]
            dp[i&1][i] = dp[1-(i&1)][i-1] + triangle[i][i]
        return min(dp[1-(len(triangle)&1)])