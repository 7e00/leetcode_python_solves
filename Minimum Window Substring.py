#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: Minimum Window Substring.py
# Author: narutoacm
# Mail: narutoacm@gmail.com
# Website: www.narutoacm.com
#########################################################################
class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(S) < len(T):
            return ""
        tcnt = [0 for i in range(256)]
        for x in T:
            tcnt[ord(x)] += 1
        scnt = [0 for i in range(256)]
        num = 0
        f = 0
        minw = len(S)+1
        minf = 0
        for i in range(len(S)):
            scnt[ord(S[i])] += 1
            if scnt[ord(S[i])] >= tcnt[ord(S[i])]:
                if scnt[ord(S[i])] == tcnt[ord(S[i])]:
                    num += scnt[ord(S[i])]
                while f < i:
                    if scnt[ord(S[f])]-1 >= tcnt[ord(S[f])]:
                        scnt[ord(S[f])] -= 1
                        f += 1
                    else:
                        break
                if num >= len(T):
                    if i-f+1 < minw:
                        minw = i-f+1
                        minf = f
        if minw > len(S):
            return ""
        else:
            return S[minf:minf+minw]
