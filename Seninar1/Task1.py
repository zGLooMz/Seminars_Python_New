# 1.Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def table():
    print('Таблица умножения')
    
    for i in range(2, 11):
        for k in range(2, 6):
            print(f'{k} x {i} = {i * k}\t', end='')
        print('')
    print('')
    for i in range(2, 11):    
        for k in range(6, 10):
            print(f'{k} x {i} = {i * k}\t', end='')
        print('')
table()