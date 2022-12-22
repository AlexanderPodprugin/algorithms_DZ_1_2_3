def twoCitySchedCost(costs):
    d_a = [] # инициализируем списки 
    d_b = []
    min_sum = 0
    for i in costs: # обход costs
        min_sum += min(i) #Прибавить i
        if i[0] > i[1]: #Если 0 элемент списка i больше первого, добавить в список разницу между ними  
            d_b.append(i[0] - i[1])
        else: #Иначе
            d_a.append(i[1] - i[0])
        
    d_a.sort() # Сортировка списков
    d_b.sort()
       
    if len(d_a) > len(d_b): # Записываем разницу между ними 
        difference_len = (len(d_a) - len(d_b)) // 2
        for i in range(difference_len): # Обход
            min_sum += d_a[0] # к min_sum прибавляем первый элемент и удаляем из списка
            d_a.pop(0)
        
    elif len(d_a) < len(d_b): # если d_a < d_b, Записываем разницу между ними 
        difference_len = (len(d_b) - len(d_a)) // 2
        for i in range(difference_len): # обход
            min_sum += d_b[0] # к min_sum прибавляем первый элемент и удаляем из списка 
            d_b.pop(0)
       
    return min_sum

"""Сложность O(n)"""