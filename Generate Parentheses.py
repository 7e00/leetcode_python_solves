class Solution:
    def gen(self, n, num):
        if num == n*2:
            if self.top == 0:
                self.reslist.append("".join(self.sta))
            return
        if self.top == n:
            self.sta[num] = ')'
            self.top -= 1
            self.gen(n, num+1)
            self.top += 1
        else:
            self.sta[num] = '('
            self.top += 1
            self.gen(n, num+1)
            self.top -= 1
            if self.top > 0:
                self.sta[num] = ')'
                self.top -= 1
                self.gen(n, num+1)
                self.top += 1
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.sta = [None]*(n*2)
        self.top = 0
        self.reslist = []
        self.gen(n, 0)
        return self.reslist
