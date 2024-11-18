import random

def get_matrix(n, m, value):

    matrix = []

    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value[j])


    return matrix


val = []
for k in range(6):
    val.append(random.randint(1, 100))

print(get_matrix(5, 6, val))
