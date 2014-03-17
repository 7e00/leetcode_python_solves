class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        length = min([len(s) for s in strs])
        if length == 0:
            return ""
        for i in range(len(strs)):
            if strs[i][0] != strs[0][0]:
                return ""
        l = 0
        r = length - 1
        while l < r:
            mid = (l+r+1)//2
            for i in range(l,mid+1):
                for j in range(len(strs)):
                    if strs[j][i] != strs[0][i]:
                        break
                else:
                    j = len(strs)
                if j != len(strs):
                    r = i-1
                    break
            else:
                l = mid
        return strs[0][:r+1]