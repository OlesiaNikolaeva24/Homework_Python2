# 1
first, second, third = int(input('Введите 1 число: ')), int(input('Введите 2 число: ')), int(input('Введите 3 число: '))
if first == second == third:
    print(3)
elif second != first and second == third or first == second and first != third or first == third and first != second:
    print(2)
else:
    print(0)

# 2
set_ = {first, second, third}
if len(set_) == 1:
    print(3)
elif len(set_) == 2:
    print(2)
if len(set_) == 3:
    print(0)