class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        dirarray = [(0,1),(1,0),(0,-1),(-1,0)]
        dir = 0
        r = c = 0
        for i in range(1,n*n+1):
            matrix[r][c] = i
            r += dirarray[dir][0]
            c += dirarray[dir][1]
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] != 0:
                r -= dirarray[dir][0]
                c -= dirarray[dir][1]
                dir = (dir+1)%4
                r += dirarray[dir][0]
                c += dirarray[dir][1]
        return matrix