class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        c = [0]*(max(len(a),len(b))+1)
        for i in range(min(len(a),len(b))):
            c[i] += int(a[len(a)-i-1])+int(b[len(b)-i-1])
            c[i+1] += (c[i]>>1)
            c[i] &= 1
        for i in range(len(b),len(a)):
            c[i] += int(a[len(a)-i-1])
            c[i+1] += (c[i]>>1)
            c[i] &= 1
        for i in range(len(a),len(b)):
            c[i] += int(b[len(b)-i-1])
            c[i+1] += (c[i]>>1)
            c[i] &= 1
        i = max(len(a),len(b))
        while i>= 0 and c[i] == 0:
            i -= 1
        if i < 0:
            return "0"
        return "".join([str(c[j]) for j in range(i,-1,-1)])