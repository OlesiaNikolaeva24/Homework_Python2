# Объявите функцию get_matrix и напишите в ней параметры n, m и value.
# Создайте пустой список matrix внутри функции get_matrix.
# Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
# В первом цикле добавляйте пустой список в список matrix.
# Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
# Во втором цикле пополняйте ранее добавленный пустой список значениями value.
# После всех циклов верните значение переменной matrix.
# Выведите на экран(консоль) результат работы функции get_matrix.
# 1
def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        matrix.append([])
        for i in range(m):
            matrix[-1].append(value)
    return matrix

while True:
    a, b, c = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: ")), input("Введите значение: ")
    print(get_matrix(a, b, c))

# 2

def get_matrix(n, m, value):
    matrix = []
    [matrix.append([value] * m) for _ in range(n)]
    return matrix

while True:
    a, b, c = int(input("Строк: ")), int(input("Столбцов: ")), input("Значение: ")
    print(get_matrix(a, b, c))
