def insertSort(l):
    for i in range(1, len(l)):
        currentValue = l[i]
        while i > 0 and l[i-1] > currentValue:
            l[i] = l[i-1]
            i -= 1
        l[i] = currentValue
    return l

l = [4,6,3,7,2,8,6,9]
print insertSort(l)


