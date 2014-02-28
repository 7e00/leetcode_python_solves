class Solution:
    # @return an integer
    d = {}
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        if (m,n) in self.d:
            return self.d[(m,n)]
        self.d[(m,n)] = self.d[(n,m)] = self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        return self.d[(m,n)]