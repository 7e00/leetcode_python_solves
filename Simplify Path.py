#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: Simplify Path.py
# Author: narutoacm
# Mail: narutoacm@gmail.com
# Website: www.narutoacm.com
#########################################################################
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if len(path) == 1:
            return path
        seg = path.split('/')
        res = [""]
        pos = 1
        for p in seg:
            if p == '.':
                continue
            elif p =='..':
                if pos != 1:
                    pos -= 1
            else:
                if len(p) == 0:
                    continue
                if len(res) == pos:
                    res.append(p)
                else:
                    res[pos] = p
                pos += 1
        if pos == 1:
            return "/"
        return "/".join(res[:pos])
