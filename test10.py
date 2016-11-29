def selectionSort(l):
    passTime = len(l) - 1
    for p in range(passTime, 0 , -1):
        maxItermIdx = 0
        for i in range(1, p+1):
            if l[i] > l[maxItermIdx]:
                maxItermIdx = i
        l[maxItermIdx], l[p] = l[p], l[maxItermIdx]
    return l

l = [1,6,2,7,4,5,9]
print selectionSort(l)


