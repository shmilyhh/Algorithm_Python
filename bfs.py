form queue import *
from graph import *

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = queue()
    vertQueue.enqueue(start)
    
    while(!vertQueue.isEmpty()):
        currentVertex = vertQueue.dequeue()
        for nbr in currentVertex.getConnections():
            if nbr.color == 'white':
                nbr.setColor('gray')
                vertQueue.enqueue(nbr)
                nbr.setDistance(currentVertex.getDistance() + 1)
                nbr.setPred(currentVertex)
        currentVertex.setColor('black')
    return g
        
def traverse(v):
    vertex = v
    while vertex.getPred():
        print vertex.getId()
        vertex = vertex.getPred()
    print vertex.getId()
    
    