from graph import *

"""
method: get the initial position, then find all the next positions by the legal movement,
        then convert the coordinates of the positions into the index to construct them into Vertex,
        then use the graph method addEdge() to connect all the next positions' nodes with the initial 
        position's node
"""

def knightGraph(bdSize):
    ktGraph = Graph()
    
    for row in range(bdSize):
        for col in range(bdSize):
            vertexId = posToId(row, col, bdSize)
            newPositions = getLegalPositions(row, col, bdSize)
            for p in newPositions:
                nid = posToId(p[0], p[1], bdSize)
                ktGraph.addEdge(vertexId, nid)
    return ktGraph
    
def posToId(row, column, bdSize):
    return row * bdSize + column
    
def getLegalPositions(row, column, bdSize):
    newPositions = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    
    for m in moveOffsets:
        newX = row + m[0]
        newY = row + m[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newPositions.append((newX, newY))
    
    return newPositions
    
def legalCoord(x, bdsize):
    if x >= 0 and x < bdsize:
        return True
    else:
        return False
        
for i in knightGraph(5):
    print i