class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        dic = {s[0]:0}
        pi = 0
        best = 0
        for i in range(1,len(s)):
            if s[i] in dic:
                if i - pi > best:
                    best = i-pi
                for j in range(pi,dic[s[i]]):
                    del dic[s[j]]
                pi = dic[s[i]]+1
                dic[s[i]] = i
            else:
                dic[s[i]] = i
        if len(s)-pi > best:
            best = len(s)-pi
        return best