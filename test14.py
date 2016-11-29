def partition(alist, first, last):
    pivot = alist[first]
    leftMark = first + 1
    rightMark = last
    done = False

    while not done:
        while alist[leftMark] <= pivot and leftMark <= rightMark:
            leftMark += 1

        while alist[rightMark] >= pivot and leftMark <= rightMark:
            rightMark -= 1


        if rightMark < leftMark:
            done = True
        else:
            alist[leftMark], alist[rightMark] = alist[rightMark], alist[leftMark]

    alist[first], alist[rightMark] = alist[rightMark], alist[first]

    return rightMark

def quickSort(alist, first, last):
    if first < last:
        m = partition(alist, first, last)
        quickSort(alist, first, m-1)
        quickSort(alist, m+1 , last)

def quickSortHelper(alist):
    quickSort(alist, 0, len(alist)-1)

alist = [54,26,93,17,77,31,44,55,20]
quickSortHelper(alist)
print(alist)
