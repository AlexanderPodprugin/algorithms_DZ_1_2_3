def getDescentPeriods(prices):
    result = 0
    l = 0
    for i in range(len(prices)):
        l += 1
        if (i+1 == len(prices)) or (prices[i]-1 != prices[i+1]):
            result += l*(l+1)//2
            l = 0

    return result   


print(getDescentPeriods([7,1,5,3,6,4]))
print(getDescentPeriods([1,2,3,4,5]))
print(getDescentPeriods([7,6,4,3,1]))