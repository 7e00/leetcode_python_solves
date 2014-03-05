# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def cloneNode(self, node):
        cnode = UndirectedGraphNode(node.label)
        self.dic[cnode.label] = cnode
        for nei in node.neighbors:
            if nei.label in self.dic:
                cnode.neighbors.append(self.dic[nei.label])
            else:
                cnode.neighbors.append(self.cloneNode(nei))
        return cnode
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        self.dic = {}
        return self.cloneNode(node)