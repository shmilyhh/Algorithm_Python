def bubbleSort(s):
    passTime = len(s) - 1
    for p in range(passTime, 0, -1):
        for i in range(p):
            if s[i] > s[i+1]:
                tmp = s[i]
                s[i] = s[i+1]
                s[i+1] = tmp
    return s

s = [4,5,3,2,6,9,7,1]
print bubbleSort(s)

def bubbleSortShortCut(s):
    passTime = len(s) - 1
    swap = True
    while swap and passTime > 0:
        swap = False
        for i in range(passTime):
            if s[i] > s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
                swap = True
        # if the whole list need to sort, it will have one more pass
        # this is to avoid one more pass
        passTime -= 1
    return s

s = [2,3,1,4,5,6]
print bubbleSortShortCut(s)
