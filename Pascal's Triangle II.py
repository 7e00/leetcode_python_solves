class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        p = [[1 for i in range(rowIndex+1)] for j in range(2)]
        for i in range(1,rowIndex+1):
            for j in range(1, i):
                p[i&1][j] = p[1-(i&1)][j-1]+p[1-(i&1)][j]
        return p[rowIndex&1]