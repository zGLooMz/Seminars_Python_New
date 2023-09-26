# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

date_st = input('Введите дату в формате DD.MM.YYYY: ')

def _is_leap_year(year):
    return year % 4 == 0 or year % 100 == 0 and year % 400 != 0

def is_valis_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    if year in range(1, 9999 + 1):
        if month in ["01", "03", "05", "07", "08", "10", "12"]:
            if day in range(1, 32):
                return True
            else:
                return False
        elif month != "02":
            if day in range(1, 31):
                return True
            else:
                return False
        else:
            if _is_leap_year(year):
                if int(day) in range(1, 30):
                    return True
                else:
                    return False
            elif int(day) in range(1, 29):
                return True
            else:
                return False
    else:
        return False


print(is_valis_date(date_st))