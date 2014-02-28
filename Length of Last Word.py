class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        l = s.split()
        if len(l) == 0:
            return 0
        return len(l[len(l)-1])