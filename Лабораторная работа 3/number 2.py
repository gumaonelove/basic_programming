'''
Задание 2. Варианты заданий на перемещение элементов списка.
Элементы списка вводить с помощью генератора случайный чисел.

8. В одномерном списке A=(a1, а2, ..., аn) все положительные элементы, имеющие четный
порядковый номер, переписать в начало списка.
'''
from functions import get_list

our_list = get_list()

new_list_1, new_list_2 = [], []
for i in range(0, len(our_list)):
    if i%2==0:
        new_list_2.append(our_list[i])
    else:
        new_list_1.append(our_list[i])
print(our_list)
print(new_list_2+new_list_1)