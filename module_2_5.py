def get_matrix(n, m, value):
    matrix = []
    [matrix.append([value] * m) for _ in range(n)]
    return matrix

while True:
    a, b, c = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: ")), int(input("Введите значение: "))
    print(*get_matrix(a, b, c))
