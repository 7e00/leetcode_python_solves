class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(0,len(grid)):
            dp[i][0] = grid[0][0] if i == 0 else dp[i-1][0] + grid[i][0]
            for j in range(1,len(grid[0])):
                dp[i][j] = dp[i][j-1]+grid[i][j]
                if i > 0 and dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
        return dp[len(grid)-1][len(grid[0])-1]