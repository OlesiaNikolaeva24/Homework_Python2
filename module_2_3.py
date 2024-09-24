# Способ 1 (while, continue, break)
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list1 = my_list[:]
while len(my_list1) != 0:
    if my_list1[0] > 0:
        print(my_list1[0])
        del my_list1[0]
        continue
    elif my_list1[0] == 0:
        del my_list1[0]
        continue
    else:
        break

print()

# Способ 2 (while, .pop())
my_list2 = my_list.copy()
while len(my_list2) != 0 and my_list2[0] >= 0:
    a = my_list2.pop(0)
    if a == 0:
        continue
    else:
        print(a)