def rock(jewels, stone): # вводим функцию
    count_jewels = 0 # начальное значение счетчика
    for i in jewels: # цикл по драгоценным камням
        if i in stone: # если драгоценный камень есть в нашей коллекции 
            count_jewels += stone.count(i) # ищем количество драгоценных камней 
    return count_jewels # возвращаем значение 

jewels = input("jewels = ")
stone = input("stone = ")
print(rock(jewels, stone))


""" Сложность - O(n)"""