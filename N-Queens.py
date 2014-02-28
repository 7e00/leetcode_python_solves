class Solution:
    def dfs(self, n, row):
        if row == n:
            maze = [["."]*n for j in range(n)]
            for i in range(n):
                maze[i][self.rows[i]] = "Q"
            self.solist.append(["".join(row) for row in maze])
            return
        for i in range(n):
            if self.selcols[i]:
                continue
            if self.seldash[row+i]:
                continue
            if self.selidash[row+n-i-1]:
                continue
            self.rows[row] = i
            self.selcols[i] = True
            self.seldash[row+i] = True
            self.selidash[row+n-i-1] = True
            self.dfs(n, row+1)
            self.selcols[i] = False
            self.seldash[row+i] = False
            self.selidash[row+n-i-1] = False
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.solist = []
        self.rows = [0 for i in range(n)]
        self.selcols = [False for i in range(n)]
        self.seldash = [False for i in range(2*n-1)]
        self.selidash = [False for i in range(2*n-1)]
        self.dfs(n, 0)
        return self.solist