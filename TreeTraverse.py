from Tree import *
from parseMathExprTree import *

def preOrder(tree):
    if tree:
        print tree.getRootValue()
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())

pt = parseTree("( ( 10 + 5 ) * 3 )")
print preOrder(pt)

def postOrder(tree):
    if tree:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print tree.getRootValue()

print postOrder(pt)
