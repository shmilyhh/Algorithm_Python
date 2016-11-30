import sys

# add new features
class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0
        
    def addNeighbor(self, nbr, weight):
        self.connectedTo[nbr] = weight
        
    def setColor(self, color):
        self.color = color
    
    def setDistance(self, d):
        self.dist = d
        
    def setPred(self, p):
        self.pred = p
        
    def setDiscovery(self, dtime):
        self.disc = dtime
        
    def setFinish(self, ftime):
        self.fin = ftime
            
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getFinish(self):
        return self.fin
    
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
    
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color        
        
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            tmp = self.addVertex(f)
        if t not in self.vertList:
            tmp = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

def buildGraph(wordFile):
    g = Graph()
    d = {}
    words = open(wordFile, 'r')
    
    # build a dictionary based on the bucket
    for line in words:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d.keys():
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    
    # add edges for words in the same bucket
    for bucket in d.keys():
        for w1 in d[bucket]:
            for w2 in d[bucket]:
                if w1 != w2:
                    g.addEdge(w1, w2)
    return g







        
"""
g = Graph()
for i in range(6):
    g.addVertex(i)
g.vertList

g.addEdge(0,1,4)
g.addEdge(0,2,5)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for w in v.getConnections():
        print "( %s, %s )" % (v.getId(), w.getId())
"""
        