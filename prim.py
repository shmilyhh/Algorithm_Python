from pythonds.graphs import PriorityQueue, Graph, Vertex

def prim(G, start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    G.setDistance(0)
    pq.buildHeap([(v.getDistance, v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nbr in currentVert.getConnections():
            newDist = currentVert.getWeight(nbr) + currentVert.getDistance()
            # remain a tree and no cycle
            if nbr in pq and newDist < nbr.getDistance():
                nbr.setDistance(newDist)
                nbr.setPred(currentVert)
                pq.decreaseKey(nbr, newDist)
                