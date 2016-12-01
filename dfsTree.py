from graph import *

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
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