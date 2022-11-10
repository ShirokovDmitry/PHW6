# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from functools import reduce
s = [9, 16, 1, 4, 32, 19, 21, 13, 11]

# b = []
# count = 0
# for i in s:
#     if count % 2 == 1:
#         b.append(i)
#     count +=1
# v = reduce(lambda x, y: x + y, b)
# print(v)

# или простой вариант

lst = list(map(int, s))
print(sum(lst[1::2]))