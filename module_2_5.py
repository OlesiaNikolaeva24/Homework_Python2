# 1
def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        matrix.append([])
        for i in range(m):
            matrix[-1].append(value)
    return matrix

while True:
    a, b, c = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: ")), int(input("Введите значение: "))
    if c <= 0:
        print([])
    else:
        print(get_matrix(a, b, c))


# 2

def get_matrix(n, m, value):
    matrix = []
    [matrix.append([value] * m) for _ in range(n)]
    return matrix

while True:
    a, b, c = int(input("Строк: ")), int(input("Столбцов: ")), int(input("Значение: "))
    if c <= 0:
        print([])
    else:
        print(get_matrix(a, b, c))
