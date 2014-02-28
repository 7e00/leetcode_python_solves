class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        p = []
        for i in range(0,numRows):
            c = [1]
            for j in range(1, i):
                c.append(p[i-1][j-1]+p[i-1][j])
            if i >= 1:
                c.append(1)
            p.append(c)
        return p