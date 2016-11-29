class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def procUp(self, i):
        while i // 2:
            if self.heapList[i//2] > self.heapList[i]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2

    def insert(self, value):
        self.heapList.append(value)
        self.currentSize += 1
        self.procUp(self.currentSize)

    def procDown(self, i):
        while i * 2 < self.currentSize:
            minChild = self.minValue(i)
            if self.heapList[i] > self.heapList[minChild]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
            i = minChild

    def minValue(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        elif self.heapList[i*2] < self.heapList[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1

    def delMin(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.procDown(1)
        return retVal

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.procDown(i)
            i -= 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print bh.delMin()
print bh.delMin()
print bh.delMin()
print bh.delMin()
print bh.delMin()
