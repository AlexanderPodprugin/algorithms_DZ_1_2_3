def uniquePaths(array_matrix):
    for i in range(1, len(array_matrix)):
        for j in range(1, len(array_matrix[i])):
            array_matrix[i][j] *= min(array_matrix[i - 1][j], array_matrix[i][j - 1], array_matrix[i - 1][j - 1]) + 1
    return sum(map(sum, array_matrix))

print(uniquePaths([[0,1,1,1],[1,1,1,1],[0,1,1,1]])) 
print(uniquePaths([[1,0,1],[1,1,0],[1,1,0]])) 





