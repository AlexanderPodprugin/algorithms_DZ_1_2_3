
def getMaximumGenerated(n): 
    array = list()
    for i in range(n+1): # Запускаем цикл, который перебирает от 0 до n + 1 
        if i == 0:
            array.append(0) # Если число 0, то добавляем 0
        elif i == 1: 
            array.append(1) #Если число 1, то добавляем 1
        elif i % 2 == 0: # Проверяем i на четность 
            array.append(array[i // 2]) # Если четное, то добавляем значение под индексом i // 2
        else:
            array.append(array[i // 2] + array[(i // 2) + 1]) # Иначе, добавляем сумму элементов под индексами i // 2 + 1 И i // 2  

    return max(array) # Возвращаем максимум 

print(getMaximumGenerated(7))
print(getMaximumGenerated(2))
print(getMaximumGenerated(3))

"""Сложность O(n)"""