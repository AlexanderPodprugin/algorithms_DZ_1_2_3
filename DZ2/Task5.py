def robot(obstacleGrid):            
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])        
        
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1:
                obstacleGrid[i][0] = 1 
            else: 0
         
        for i in range(1,n):
            if obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1:
                obstacleGrid[0][i] = 1
            else: 0
            
        for row in range(1, m):
            for col in range(1, n):                
                if obstacleGrid[row][col] == 0:
                    obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]
                else: 0
         
        return obstacleGrid[-1][-1]

print(robot([[0,0,0],[0,1,0],[0,0,0]]))
print(robot([[0,1],[0,0]]))