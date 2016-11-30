"""
method: use dfs method to solve this problem,
        n, the dpeth of the current status
        path, the list of current vertices
        u, the explore vertex
        limit, the max number of the vertices

        base case: if the len(path) >= limit, return True
                   else continue recursively call method
        
        if the method returns False, backtrack and try another adjacent vertex
        use color to mark the vertex to see whether it is visited
"""
from knightMove import *

def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if len(path) < limit:
        #adjacentVertices = u.getConnections()
        adjacentVertices = orderByAvail(u)
        i = 0
        done = False
        while i < len(adjacentVertices) and not done:
            if adjacentVertices[i].getColor() == 'white':
                done = knightTour(n+1, path, adjacentVertices[i], limit) 
            i += 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
        
    return done


def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [x[1] for x in resList]


    
g = knightGraph(8)
for i in g:
    a = i
    break
path = []
knightTour(0, path, a, 63)