def convertToStringInAnyBase(num, base, baseList):
    if num < base:
        return baseList[num]

    return convertToStringInAnyBase(num/base, base, baseList) + baseList[num%base]

print convertToStringInAnyBase(12345, 10, '0123456789')
print convertToStringInAnyBase(1453, 16, '0123456789ABCDEF')
print convertToStringInAnyBase(1345, 2, '01')


