class Solution:
    def uniquePath(self, obstacleGrid, r, c):
        if obstacleGrid[r][c] == 1:
            return 0
        if self.d[r][c] != -1:
            return self.d[r][c]
        if r == 0:
            for i in range(0,c):
                if obstacleGrid[r][i] == 1:
                    self.d[r][c] = 0
                    return 0
            self.d[r][c] = 1
            return 1
        if c == 0:
            for i in range(0,r):
                if obstacleGrid[i][c] == 1:
                    self.d[r][c] = 0
                    return 0
            self.d[r][c] = 1
            return 1
        self.d[r][c] = self.uniquePath(obstacleGrid, r-1, c) + self.uniquePath(obstacleGrid, r, c-1)
        return self.d[r][c]
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        self.d = [[-1 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        return self.uniquePath(obstacleGrid, len(obstacleGrid)-1, len(obstacleGrid[0])-1)