class Solution:
    def dfs(self, n, row):
        if row == n:
            self.sols += 1
            return
        for i in range(n):
            if self.selcols[i]:
                continue
            if self.seldash[row+i]:
                continue
            if self.selidash[row+n-i-1]:
                continue
            self.selcols[i] = True
            self.seldash[row+i] = True
            self.selidash[row+n-i-1] = True
            self.dfs(n, row+1)
            self.selcols[i] = False
            self.seldash[row+i] = False
            self.selidash[row+n-i-1] = False
    # @return an integer
    def totalNQueens(self, n):
        self.selcols = [False for i in range(n)]
        self.seldash = [False for i in range(2*n-1)]
        self.selidash = [False for i in range(2*n-1)]
        self.sols = 0
        self.dfs(n, 0)
        return self.sols