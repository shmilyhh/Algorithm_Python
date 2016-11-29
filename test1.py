def sumListReverse(alist):
    if len(alist) == 0:
        return 0
    result = alist[0] + sumListReverse(alist[1:])
    print "current number", alist[0]
    return result

a = [1,2,3,4,5]
print sumListReverse(a)


def sumListInOrder(alist):
    if len(alist) == 0:
        return 0

    result = alist[-1] + sumListInOrder(alist[:len(alist)-1])
    print "current number", alist[-1]
    return result

r = [1,2,3,4,5]
print sumListInOrder(r)
