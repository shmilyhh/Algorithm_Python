from Tree import *
from Stack import *
import operator

def parseTree(expr):
    exprList = expr.split()
    r = Tree('')
    s = Stack()
    s.push(r)
    currentTree = r

    for i in exprList:
        if i == '(':
            currentTree.inserLeft('')
            s.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootValue(int(i))
            currentTree = s.pop()
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootValue(i)
            currentTree.inserRight('')
            s.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = s.pop()
        else:
            raise ValueError
    return r

pt = parseTree("( ( 10 + 5 ) * 3 )")
print pt.getRootValue()

def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    currentTree = parseTree
    left = currentTree.getLeftChild()
    right = currentTree.getRightChild()

    if left and right:
        fn = opers[currentTree.getRootValue()]
        return fn(evaluate(left), evaluate(right))
    else:
        return currentTree.getRootValue()

print evaluate(pt)

def evaluatePostOrder(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    
    if tree:
        left = evaluatePostOrder(tree.getLeftChild())
        right = evaluatePostOrder(tree.getRightChild())

        if left and right:
            return opers[tree.getRootValue()](left, right)
        else:
            return tree.getRootValue()
print evaluatePostOrder(pt)

def printMathExpr(tree):
    sVal = ''
    if tree and tree.getLeftChild() and tree.getRightChild():
        sVal = '(' + printMathExpr(tree.getLeftChild())
        sVal += str(tree.getRootValue())
        sVal += printMathExpr(tree.getRightChild()) + ')'
    elif tree:
        sVal = printMathExpr(tree.getLeftChild())
        sVal += str(tree.getRootValue())
        sVal += printMathExpr(tree.getRightChild())
    return sVal

print printMathExpr(pt)
