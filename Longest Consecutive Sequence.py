class Solution:
    # @param num, a list of integer
    # @return an integer
    def get_inf(self, inf, x):
        if x-1 in inf:
            res = self.get_inf(inf, inf[x-1])
            inf[x-1] = res
            return res
        else:
            return x
    def get_sup(self, sup, x):
        if x+1 in sup:
            res = self.get_sup(sup, sup[x+1])
            sup[x+1] = res
            return res
        else:
            return x
    def longestConsecutive(self, num):
        inf = {}
        sup = {}
        maxlen = 0
        for x in num:
            if x in inf:
                continue
            inf[x] = self.get_inf(inf, x)
            sup[x] = self.get_sup(sup, x)
            if maxlen < (sup[x] - inf[x] + 1):
                maxlen = sup[x] - inf[x] + 1
        return maxlen