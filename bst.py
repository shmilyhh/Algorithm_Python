class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
        
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        return self.put(k, v)
    
    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, k):
        return self.get(k)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToDel = self._get(key, self.root)
            if nodeToDel:
                self.remove(nodeToDel)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.szie -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: # only have one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent
                else:
                    currentNode.replaceNodeData(currentNode.key,
                                                currentNode.payload,
                                                currentNode.leftChild,
                                                currentNode.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent
                else:
                    currentNode.replaceNodeData(currentNode.key,
                                                currentNode.payload,
                                                currentNode.leftChild,
                                                currentNode.rightChild)



class TreeNode():
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not(self.leftChild or self.rightChild)

    def hasAntChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.payload = key
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    

    def findSuccessor(self): 
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.rightChild = None
        elif self.hasAntChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

"""                
mytree = BinarySearchTree()
mytree[3] = 'red'
mytree[5] = 'blue'
mytree[1] = 'at'
mytree[4] = 'green'
mytree[6] = 'yellow'

print 3 in mytree
print 4 in mytree
print 6 in mytree
print 2 in mytree
mytree.delete(3)
print mytree.root.key
"""