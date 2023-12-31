# 3. Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%».

# В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

names = ['Alex', 'Leo', 'Bill', "Robert"]
salaries = [9000, 11000, 18000, 7000]
awards = ['8.35%', '11.25%', '9.75%', '10.85%']

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})