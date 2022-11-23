def uniquePaths(array_matrix): #Запускаем цикл, который идет по двумерному массиву 
    for i in range(1, len(array_matrix)): #Запускаем цикл, который идет по элементам массива 
        for j in range(1, len(array_matrix[i])):#Записываем в ячейку массива минимальное значение из соседних ячеек 
            array_matrix[i][j] *= min(array_matrix[i - 1][j], array_matrix[i][j - 1], array_matrix[i - 1][j - 1]) + 1
    return sum(map(sum, array_matrix))#Возвращаем сумму всех единиц 

print(uniquePaths([[0,1,1,1],[1,1,1,1],[0,1,1,1]])) 
print(uniquePaths([[1,0,1],[1,1,0],[1,1,0]])) 



"""Сложность O(n**2)"""

