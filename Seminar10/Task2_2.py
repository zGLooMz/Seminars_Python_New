
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.


class Year:
    def __init__(self, txt):
        self.str_data = txt
        self.day, self.month, self.year = self.str_data.split(".")


    def check_date(self):
        if int(self.year) in range(1, 9999 + 1):
            if self.month in ["01", "03", "05", "07", "08", "10", "12"]:
                if int(self.day) in range(1, 32):
                    return True
                else:
                    return False
            elif self.month != "02":
                if int(self.day) in range(1, 31):
                    return True
                else:
                    return False
            else:
                if int(self.year) % 400 == 0 or int(self.year) % 4 == 0 and int(self.year) % 100 != 0:
                    if int(self.day) in range(1, 30):
                        return True
                    else:
                        return False
                elif int(self.day) in range(1, 29):
                    return True
                else:
                    return False
        else:
            return False


y = Year("01.10.2023")
print(y.check_date())