def mergeSort(aList):
    print "Splitting ", aList
    if len(aList) > 1:
        midPoint = len(aList) // 2
        leftList = aList[:midPoint]
        rightList = aList[midPoint:]

        mergeSort(leftList)
        mergeSort(rightList)

        i = 0
        j = 0
        k = 0

        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                aList[k] = leftList[i]
                i += 1
            else:
                aList[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList):
            aList[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            aList[k] = rightList[j]
            j += 1
            k += 1

        print "Merging ", aList

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

