# Напишите следующие функции:
#
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import json
import csv
import os
import random
from math import sqrt


def gen_csv(num=3, start_num=1, end_num=100, quantity_min=100, quantity_max=1000):
    with open("randomlist.csv", "w", encoding="utf-8", newline="") as js:
        writer = csv.writer(js, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows([[random.randint(start_num, end_num) for _ in range(num)] for _ in
                          range(random.randint(quantity_min, quantity_max))])


def save_vareables(func):
    def wrapper(*args, **qargs):
        if os.path.exists(func.__name__ + ".json"):
            with open(func.__name__ + ".json", "r", encoding='utf-8') as res_f:
                res = json.load(res_f)
        else:
            res = []
        res.append({"args": [*args, *qargs], "result": (func(*args, **qargs))})
        with open(func.__name__ + ".json", "w", encoding='utf-8') as result_f:
            json.dump(res, result_f, indent=1)
        return func

    return wrapper


def csv_variable(func):
    def wrapper(*args, **qargs):

        if os.path.exists("randomlist.csv"):
            with open("randomlist.csv", encoding='utf-8', newline="") as res_f:
                for item in csv.reader(res_f, quoting=csv.QUOTE_NONNUMERIC):
                    func(*item)

                return func
        else:
            return func

    return wrapper


@csv_variable
@save_vareables
def check(a, b, c):

    disc = b * b - 4 * a * c
    if disc < 0:
        return False
    else:
        root = sqrt(disc)  
        x_1 = (-b + root) / (2 * a)  
        if disc != 0:  
            x_2 = (-b - root) / (2 * a)  
            return x_1, x_2
        else:
            return x_1


gen_csv()
check('randomlist.csv')