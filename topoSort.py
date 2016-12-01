from graph import *

class DFSGraph(Graph, object):
    def __init__(self):
        super(DFSGraph, self).__init__()
        self.time = 0
        
    def dfs(self):
        for v in self:
            v.setColor('white')
            v.setPred(-1)
        for v in self:
            if v.getColor() == 'white':
                self.dfsvisit(v)
    
    def dfsvisit(self, vertex):
        vertex.setColor('gray')
        self.time += 1
        vertex.setDiscovery(self.time)
        nbrs = vertex.getConnections()
        for nbr in nbrs:
            if nbr.getColor() == 'white':
                nbr.setPred(vertex)
                self.dfsvisit(nbr)
        vertex.setColor('black')
        self.time += 1
        vertex.setFinish(self.time)
        
    def topoSort(self):
        self.dfs()
        results = []
        for v in self:
            results.append(v)
        results.sort(key=lambda x: x.getFinish())
        results.reverse()
        return results
        
g = DFSGraph()
for i in range(9):
    g.addVertex(i)
    
g.addEdge(0, 3)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(5, 4)
g.addEdge(4, 6)
g.addEdge(6, 7)
g.addEdge(3, 8)
g.addEdge(8, 7)

for i in g.topoSort():
    print i
