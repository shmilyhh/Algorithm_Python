class Tree():
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def inserLeft(self, newNode):
        if self.left == None:
            self.left = Tree(newNode)
        else:
            t = Tree(newNode)
            t.left = self.left
            self.left = t
    
    def inserRight(self, newNode):
        if self.right == None:
            self.right = Tree(newNode)
        else:
            t = Tree(newNode)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootValue(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key

def buildTree():
    a = Tree('a')
    a.inserLeft('b')
    a.getLeftChild().inserLeft('d')
    a.inserRight('c')
    a.getRightChild().inserLeft('e')
    a.getRightChild().inserRight('f')
    
    return a



