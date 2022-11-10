# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
from math import factorial
n = int(input('Введите число: '))
s = list(range(1, int(n)+1))
x = list(map(lambda x: x * factorial(x -1), s))
print(x)
