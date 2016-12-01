from pythonds.graphs import PriorityQueue, Graph, Vertex

def dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.setDistamce(0)
    pq.buildHeap([(v.getDistance, v) for v in aGraph])
    while not pq.isEmpty():
        currentVertex = pq.delMin()
        for nbr in currentVertex.getConnections():
            newDist = currentVertex.getDistance() + currentVertex.getWeight(nbr)
            if newDist < nbr.getDistance():
                nbr.setPred(currentVertex)
                nbr.setDistance(newDist)
                pq.decreaseKey(nbr, newDist)
        