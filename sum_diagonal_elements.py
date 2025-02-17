def sum_diagonal_elements(matrix):
    size = len(matrix)
    sum_diagonal = 0
    for i in range(size):
        sum_diagonal += matrix[i][i]
    return sum_diagonal

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


sum_diagonal = sum_diagonal_elements(matrix)


print("Sum of diagonal elements:", sum_diagonal)