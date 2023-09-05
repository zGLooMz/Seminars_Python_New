# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions

fract_1 = input("Введите первую дробь в формате a/b: ").split("/")
fract_2 = input("Введите вторую дробь в формате c/d: ").split("/")

common_denominator = int(fract_1[1]) * int(fract_2[1])
a = int(fract_1[0]) * int(fract_2[1]) + int(fract_2[0]) * int(fract_1[1])
sum_of_fractions = f"{a}/{common_denominator}"

numer = int(fract_1[0]) * int(fract_2[0])
denom = int(fract_1[1]) * int(fract_2[1])
product_of_fractions = f"{numer}/{denom}"

print(f"Сумма дробей: {sum_of_fractions}")
print(f"Произведение дробей: {product_of_fractions}")

print("\nПроверка при помощи <fractions>")
f1 = fractions.Fraction(int(fract_1[0]), int(fract_1[1]))
f2 = fractions.Fraction(int(fract_2[0]), int(fract_2[1]))
print(f"Сумма дробей: {f1 + f2}")
print(f"Произведение дробей: {f1 * f2}")