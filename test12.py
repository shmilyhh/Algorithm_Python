def shellSort(l):
    subproblemCount = len(l) // 2

    while subproblemCount > 0:
        for i in range(subproblemCount):
            gapInsertSort(l, i, subproblemCount)
        
        print "After increment of the size, the size is", subproblemCount, "current sorted list", l
        subproblemCount = subproblemCount // 2

def gapInsertSort(l, start, gap):
    for i in range(start+gap, len(l), gap):
        currentValue = l[i]
        while i >= gap and l[i-gap] > currentValue:
            l[i] = l[i-gap]
            i -= gap
        l[i] = currentValue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
