class PriorityQueue():
    def __init__(self):
        self.heapArray = [(0, 0)]
        self.currentSize = 0

    def procUp(self, i):
        while i // 2:
            if self.heapArray[i//2][0] > self.heapArray[i][0]:
                self.heapArray[i][0], self.heapArray[i//2][0] = self.heapArray[i//2][0], self.heapArray[i][0]
            i = i // 2

    def insert(self, value):
        self.heapArray.append(value)
        self.currentSize += 1
        self.procUp(self.currentSize)

    def procDown(self, i):
        while i * 2 < self.currentSize:
            minChild = self.minValue(i)
            if self.heapArray[i][0] > self.heapArray[minChild][0]:
                self.heapArray[i], self.heapArray[minChild] = self.heapArray[minChild], self.heapArray[i]
            i = minChild

    def minValue(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        elif self.heapArray[i*2][0] < self.heapArray[i*2+1][0]:
            return i * 2
        else:
            return i * 2 + 1

    def delMin(self):
        retVal = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize -= 1
        self.heapArray.pop()
        self.procDown(1)
        return retVal

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapArray = [(0, 0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2
        while i > 0:
            self.procDown(i)
            i -= 1
    
    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False
    
    def decreaseKey(self, node, val):
        done = False
        i = 1
        key = 0
        while not done and i < self.currentSize:
            if self.heapArray[i][1] == node:
                done = True
                key = i
            i += 1
        if key > 0:
            self.heapArray[key] = (val, node)
            self.percUp(key)
    
    def __contains__(self, vertex):
        for t in self.heapArray:
            if t[1] == vertex:
                return True
        return False
        
        
bh = PriorityQueue()
bh.buildHeap([(9,'a'), (5, 'b'), (6, 'c'), (2, 'd'), (3, 'e')])

print bh.delMin()
print bh.delMin()
print bh.delMin()
print bh.delMin()
print bh.delMin()
