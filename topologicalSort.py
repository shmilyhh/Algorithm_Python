class DirectedgraphNode():
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution():
    def dfs(self, i, countrd, ans):
        ans.append(i)
        countrd[i] -= 1
        for j in i.neighbors:
            countrd[j] = countrd[j] - 1
            if countrd[j] == 0:
                self.dfs(j, countrd, ans)
                
    def topoSort(self, graph):
        countrd = {}
        for v in graph:
            countrd[v] = 0
        
        for v in graph:
            for nbr in v.neighbors:
                #print nbr
                countrd[nbr] += 1
        
        ans = []
        for i in graph:
            if countrd[i] == 0:
                self.dfs(i, countrd, ans)
        return ans
        
n0 = DirectedgraphNode(0)
n1 = DirectedgraphNode(1)
n2 = DirectedgraphNode(2)
n3 = DirectedgraphNode(3)
n4 = DirectedgraphNode(4)
n5 = DirectedgraphNode(5)
n6 = DirectedgraphNode(6)
n7 = DirectedgraphNode(7)
n8 = DirectedgraphNode(8)

n0.neighbors.append(n3)
n1.neighbors.append(n3)
n2.neighbors.append(n3)
n3.neighbors.append(n4)
n3.neighbors.append(n8)
n4.neighbors.append(n6)
n5.neighbors.append(n4)
n6.neighbors.append(n7)
n8.neighbors.append(n7)


g = [n0 ,n1, n2, n3, n4, n5, n6, n7, n8]
s = Solution()

for i in s.topoSort(g):
    print i.label
#print s.topoSort(g)
