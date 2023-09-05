# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.


def user_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result

num = int(input('Введите целое число: '))
print(f'Шестнадцатеричное строковое представление: {user_hex(num)}')
print(f'Проверка функцией hex: {hex(num)}')