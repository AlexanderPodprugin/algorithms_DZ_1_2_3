def getDescentPeriods(prices): 
    result = 0 # Счетчик 
    l = 0 #ПЕРЕМЕННАЯ
    for i in range(len(prices)): # Запускаем цикл по длине prices
        l += 1 # прибавляем 1 к переменной
        if (i+1 == len(prices)) or (prices[i]-1 != prices[i+1]): # Если мы на предпоследней итерации или prices[i]-1 != prices[i+1]
            result += l*(l+1)//2 # Обнуляем l и к результату добавляем математическое выражение += l*(l+1)//2
            l = 0

    return result   


print(getDescentPeriods([7,1,5,3,6,4]))
print(getDescentPeriods([1,2,3,4,5]))
print(getDescentPeriods([7,6,4,3,1]))


"""Сложность - O(n)"""