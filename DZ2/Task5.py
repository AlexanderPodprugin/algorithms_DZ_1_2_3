def robot(obstacleGrid): # Если 1 элемент = 1, возвращаем 0       
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0]) # Записываем в m и n длинну двумерного массива и одномерного массива         
        
        obstacleGrid[0][0] = 1 # Первый элемент равен 1
        for i in range(1,m): # Запускаем цикл от 1 до m 
            if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1: # Если есть столбик из 0, то прибавляем 1
                obstacleGrid[i][0] = 1 
            else: 0 # Иначе ноль
         
        for i in range(1,n): # Запускаем цикл от 1 до n
            if obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1: # Если есть столбик из 0, то прибавляем 1
                obstacleGrid[0][i] = 1
            else: 0
            
        for row in range(1, m): # Запускаем цикл от 1 до m, а потом до n 
            for col in range(1, n):         
                if obstacleGrid[row][col] == 0: # Если значение ячейки равно 0, добавляем соседние элементы 
                    obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]
                else: 0
         
        return obstacleGrid[-1][-1] # Возвращаем последний элемент 

print(robot([[0,0,0],[0,1,0],[0,0,0]]))
print(robot([[0,1],[0,0]]))


"""Сложность O(n**2) + O(n) + O(n)"""