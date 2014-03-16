class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return "1"
        sl = [1]
        for i in range(n-1):
            nsl = []
            prex = None
            precnt = 0
            for x in sl:
                if prex == None or x == prex:
                    precnt += 1
                    prex = x
                else:
                    nsl.append(precnt)
                    nsl.append(prex)
                    precnt = 1
                    prex = x
            else:
                nsl.append(precnt)
                nsl.append(prex)
            sl = nsl
        return ''.join([str(x) for x in sl])