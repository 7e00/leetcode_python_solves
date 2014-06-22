#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: Combinations.py
# Author: narutoacm
# Mail: narutoacm@gmail.com
# Website: www.narutoacm.com
#########################################################################
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if n == k:
            return [[i for i in range(1,n+1)]]
        if k == 1:
            return [[i] for i in range(1,n+1)]
        subreslist = self.combine(n-1,k-1)
        reslist = [[1]+[x+1 for x in each] for each in subreslist]
        subreslist = self.combine(n-1,k)
        reslist.extend([[x+1 for x in each] for each in subreslist])
        return reslist
