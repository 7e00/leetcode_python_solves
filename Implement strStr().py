class Solution:
    def naive(self, haystack, needle):
        if len(needle) == 0:
            return haystack
        i = 0
        while i <= len(haystack)-len(needle):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                else:
                    return haystack[i:]
            i += 1
        return None
    def kmp(self, haystack, needle):
        if len(needle) == 0:
            return haystack
        p = [-1]*len(needle)
        for i in range(1,len(needle)):
            j = p[i-1]
            while j != -1 and needle[i] != needle[j+1]:
                j = p[j]
            p[i] = j+1 if needle[i] == needle[j+1] else j
        j = -1
        for i in range(len(haystack)):
            while j != -1 and haystack[i] != needle[j+1]:
                j = p[j]
            j = j+1 if haystack[i] == needle[j+1] else j
            if j == len(needle)-1:
                return haystack[i-len(needle)+1:]
        return None
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        return self.kmp(haystack, needle)