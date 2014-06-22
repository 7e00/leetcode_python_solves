#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: Edit Distance.py
# Author: narutoacm
# Mail: narutoacm@gmail.com
# Website: www.narutoacm.com
#########################################################################
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        dp[0][0] = 0
        for j in range(1,len(word2)+1):
            dp[0][j] = j
        for i in range(1,len(word1)+1):
            dp[i][0] = i
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1]+1
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[len(word1)][len(word2)]
