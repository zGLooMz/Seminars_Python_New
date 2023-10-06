
# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.



class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, Кличка: {self.get_name()}, Возраст: {self.get_age()} лет,' \
               f' special: {self.get_specific()}'


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, Кличка: {self.get_name()}, Возраст: {self.get_age()} лет,' \
               f' special: {self.get_specific()}'


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, Кличка: {self.get_name()}, Возраст: {self.get_age()} лет,' \
               f' specific: {self.get_specific()}'


if __name__ == '__main__':
    f1 = Fishes('Карась', 'Джо', 2, 20)

    print(f'Вид: {f1.get_kind()}')
    print(f'Кличка: {f1.get_name()}')
    print(f'Возраст: {f1.get_age()} лет')
    print(f'Размер: {f1.get_specific()} см.')

    b1 = Birds('Воробей', 'Джек', 5, 'Коричневый')
    print(f'Вид: {b1.get_kind()}')
    print(f'Кличка: {b1.get_name()}')
    print(f'Возраст: {b1.get_age()} лет')
    print(f'Цвет: {b1.get_specific()}')