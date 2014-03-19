class Solution:
    def dfs(self, digits, n, l):
        if n == len(digits):
            self.strlist.append("".join(l))
            return
        for letter in self.dic[int(digits[n])]:
            if n == len(l):
                l.append(letter)
            else:
                l[n] = letter
            self.dfs(digits, n+1, l)
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.dic = {
                    2:('a','b','c'),
                    3:('d','e','f'),
                    4:('g','h','i'),
                    5:('j','k','l'),
                    6:('m','n','o'),
                    7:('p','q','r','s'),
                    8:('t','u','v'),
                    9:('w','x','y','z'),
                    0:(' ')
                    }
        self.strlist = []
        self.dfs(digits, 0, [])
        return self.strlist