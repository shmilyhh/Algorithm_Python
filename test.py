def recMinCoin(availableCoins, money):
    # baseline: use the penny
    minNumber = money
    # subproblems
    # recMinCoin(money-i)
    if money in availableCoins:
        return 1
        # choices
    else:
        for i in [c for c in availableCoins if c <= money]:
            # recursive
            number = recMinCoin(availableCoins, money-i) + 1
            # topo order: from the i to money
            # base case: money == i, return 1
            if number < minNumber:
                minNumber = number
    return minNumber


#a = [1,5,10,25]
#print recMinCoin(a, 63)

# Memorization
def recMinCoin(availableCoins, money, moneyList):
    # baseline: use the penny
    minNumber = money
    # subproblems
    # recMinCoin(money-i)
    if money in availableCoins:
        moneyList[money] = 1
        return 1
        # choices
    elif moneyList[money] > 0:
        return moneyList[money]
    else:
        for i in [c for c in availableCoins if c <= money]:
            # recursive
            number = recMinCoin(availableCoins, money-i, moneyList) + 1
            # topo order: from the i to money
            # base case: money == i, return 1
            if number < minNumber:
                minNumber = number
                moneyList[money] = minNumber
    return minNumber

#a = [1,5,10,25]
#b = [0] * 64
#print recMinCoin(a, 63, b)


# dp
def recMinCoin(availableCoins, money, moneyList, usedCoinList):
    # subproblems
    # recMinCoin(money-i)

    # topo orderL from 0 to money
    for j in range(1, money+1):
        # baseline
        minNumber = j
        usedCoin = 1
        # choices
        for i in [c for c in availableCoins if c <= minNumber]:
            # recursive
            number = moneyList[j-i] + 1
            # topo order: from the i to money
            # base case: money == i, return 1
            if number < minNumber:
                minNumber = number
                usedCoin = i
        moneyList[j] = minNumber
        usedCoinList[j] = usedCoin
    return moneyList


typeCoins = [1,5,10,21,25]
allMoney = [0] * 64
usedCoin = [0] * 64
print(recMinCoin(typeCoins, 63, allMoney, usedCoin))
rest = 63
print usedCoin
while rest > 0:
    coin = usedCoin[rest]
    print coin
    rest = rest - coin
