# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

from math import sqrt


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = b ** 2 - 4 * a * c

    def answer(self):
        if self.d > 0:
            x1 = (-self.b + sqrt(self.d)) / (2 * self.a)
            x2 = (-self.b - sqrt(self.d)) / (2 * self.a)
            return (f'Корни уравнения: x1 = {x1:.3f}; x2 = {x2:.3f}')
        elif self.d == 0:
            x1 = -self.b / (2 * self.a)
            return (f'Корень уравнения: x = {x1:.3f}')
        else:
            real = round(-self.b / (2 * self.a), 4)
            imaginary = round(sqrt(abs(self.d)) / (2 * self.a), 4)
            x1 = complex(real, imaginary)
            x2 = complex(real, -imaginary)
            return (f'Корни уравнения: x1 = {x1}; x2 = {x2}')


print('Решение квадратного уравнеия вида a*x**2+b*x+c=0')
a = float(input('введите значение a (с учетом знака): '))
b = float(input('введите значение b (с учетом знака): '))
c = float(input('введите значение c (с учетом знака): '))

qe = QuadraticEquation(a, b, c)
print(qe.answer())