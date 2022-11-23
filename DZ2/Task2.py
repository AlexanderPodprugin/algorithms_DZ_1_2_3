
def getMaximumGenerated(n):
    array = list()
    for i in range(n+1):
        if i == 0:
            array.append(0)
        elif i == 1:
            array.append(1)
        elif i % 2 == 0:
            array.append(array[i // 2])
        else:
            array.append(array[i // 2] + array[(i // 2) + 1])

    return max(array)

print(getMaximumGenerated(7))
print(getMaximumGenerated(2))
print(getMaximumGenerated(3))