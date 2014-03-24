class Solution:
    def remove(self, node):
        self.nxtlist[self.prelist[node]] = self.nxtlist[node]
        self.prelist[self.nxtlist[node]] = self.prelist[node]
        
    def recover(self, node):
        self.nxtlist[self.prelist[node]] = node
        self.prelist[self.nxtlist[node]] = node
        
    def permu(self, num, n, head, per):
        if n == len(num)-1:
            per[len(num)-1] = num[head]
            self.reslist.append(per[:])
            return
        self.remove(head)
        per[n] = num[head]
        self.permu(num, n+1, self.nxtlist[head], per)
        self.recover(head)
        cur = self.nxtlist[head]
        while cur != head:
            self.remove(cur)
            per[n] = num[cur]
            self.permu(num, n+1, head, per)
            self.recover(cur)
            cur = self.nxtlist[cur]
            
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.nxtlist = [(i+1)%len(num) for i in range(len(num))]
        self.prelist = [(i-1+len(num))%len(num) for i in range(len(num))]
        self.reslist = []
        self.permu(num, 0, 0, num[:])
        return self.reslist