class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2) != len(s3):
            return False
        if len(s1) > len(s2):
            s = s1
            s1 = s2
            s2 = s
        if len(s1) == 0:
            return s2 == s3
        dp = [[False for i in range(len(s1)+1)] for j in range(len(s3)+1)]
        dp[0][0] = True
        for i in range(1, len(s3)+1):
            for j in range(0, min(i+1,len(s1)+1)):
                if j > 0 and s3[i-1] == s1[j-1] and dp[i-1][j-1]:
                    dp[i][j] = True
                if not dp[i][j] and i-1 >= j and i-1-j < len(s2) and s3[i-1] == s2[i-1-j] and dp[i-1][j]:
                    dp[i][j] = True
        return dp[len(s3)][len(s1)]