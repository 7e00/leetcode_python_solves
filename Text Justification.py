class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        reslist = []
        lastpos = 0
        wlen = -1
        for i in range(len(words)):
            if len(words[i]) == 0:
                continue
            if len(words[i]) + 1 + wlen <= L:
                wlen += len(words[i]) + 1
            else:
                if i-lastpos == 1:
                    line = words[lastpos]+" "*(L-wlen)
                else:
                    bn = (L-wlen)/(i-lastpos-1)
                    lo = (L-wlen) - bn*(i-lastpos-1)
                    line = words[lastpos]
                    for j in range(lastpos+1, lastpos+1+lo):
                        line += " "*(bn+2) + words[j];
                    for j in range(lastpos+1+lo, i):
                        line += " "*(bn+1) + words[j]
                reslist.append(line)
                lastpos = i
                wlen = len(words[i])
        lastline = words[lastpos]
        if wlen == -1:
            wlen = 0;
        for i in range(lastpos+1, len(words)):
            if len(words[i]) == 0:
                continue
            lastline += " " + words[i]
        lastline += " "*(L-wlen)
        reslist.append(lastline)
        return reslist