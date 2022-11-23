def maxProfit(prices):
    counter = 0 # Счетчик 
    for i in range(1, len(prices)): # Запускаем цикл от 1 до конца длины списка 
        if prices[i] - prices[i - 1] > 0: # Если то элемент, на котором мы находимся сейчас -  тот, который был на прошлой итерации, он будет больше 0
            counter += (prices[i] - prices[i - 1]) # К счетчику прибавляем получившееся значение 
    return counter # Возвращаем счетчик 

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))


"""Сложность - O(n)"""