class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        j = 0
        ans = 0
        anss = None
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                p1 = i-1
                p2 = i
                while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                    p2 += 1
                    p1 -= 1
                if ans < p2-p1-1:
                    ans = p2-p1-1
                    anss = s[p1+1:p2]
            p1 = i-1
            p2 = i+1
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                p2 += 1
                p1 -= 1
            if ans < p2-p1-1:
                ans = p2-p1-1
                anss = s[p1+1:p2]
        return anss