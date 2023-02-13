import random

def create_matrix(t):
    a = []
    for i in range(t * t):
        while True:
            n = random.randint(1, 50)
            if n not in a:
                a.append(n)
                break
    matrix = []
    for i in range(t):
        row = []
        for j in range(t):
            row.append(a[i * t + j])
        matrix.append(row)
    return matrix

def extract_diagonal(matrix, t, direction):
    diagonal = []
    for i in range(t):
        if direction == 'left_to_right':
            diagonal.append(matrix[i][i])
        elif direction == 'right_to_left':
            diagonal.append(matrix[i][t - i - 1])
    return diagonal

matrix = create_matrix(4)
diagonal1 = extract_diagonal(matrix, 4, 'left_to_right')
diagonal2 = extract_diagonal(matrix, 4, 'right_to_left')

print(matrix)
print(diagonal1)
print(diagonal2)