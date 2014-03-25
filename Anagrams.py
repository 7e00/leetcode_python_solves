class Solution:
    def clac(self, s):
        nums = [0]*26
        for x in s:
            nums[ord(x)-97] += 1
        res = 0
        for i in range(26):
            res *= 26
            res += nums[i]
        return res
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        for i in range(len(strs)):
            key = self.clac(strs[i])
            d.setdefault(key, [])
            d[key].append(strs[i])
        res = []
        for key,val in d.items():
            if len(val) > 1:
                res.extend(val)
        return res