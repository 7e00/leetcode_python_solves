class Solution:
    # @return an integer
    def romanToInt(self, s):
        d = {
            "I":(0,1),
            "V":(1,5),
            "X":(2,10),
            "L":(3,50),
            "C":(4,100),
            "D":(5,500),
            "M":(6,1000)
            }
        res = d[s[0]][1]
        for i in range(1,len(s)):
            if d[s[i]][0] > d[s[i-1]][0]:
                res -= d[s[i-1]][1]
                res += d[s[i]][1]-d[s[i-1]][1]
            else:
                res += d[s[i]][1]
        return res