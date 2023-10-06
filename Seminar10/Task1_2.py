
# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики


from Task1_1 import Mammals, Birds, Fishes


class Fabric:

    def __init__(self, animal_class, **kwargs):
        self.animal_class = animal_class

        for key, value in kwargs.items():
            if key == 'kind':
                self.kind = value
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'color':
                self.color = value
            if key == 'spec':
                self.spec = value
            if key == 'size':
                self.size = value

    def get_info(self):
        if self.animal_class == 'bird':
            return Birds(self.kind, self.name, self.age, self.color)
        elif self.animal_class == 'mammal':
            return Mammals(self.kind, self.name, self.age, self.spec)
        elif self.animal_class == 'fish':
            return Fishes(self.kind, self.name, self.age, self.size)


if __name__ == '__main__':
    animal1 = Fabric(animal_class='bird', kind='Ворон', name='Карл', age=2, color='черный')
    print(animal1.get_info().get_animal_info())

    animal2 = Fabric(animal_class='mammal', kind='Кит', name='Вилли', age=5, spec='косатка')
    print(animal2.get_info().get_animal_info())

    animal3 = Fabric(animal_class='mammal', kind='Кот', name='Леопольд', age=3, spec='Греческая')
    print(animal3.get_info().get_animal_info())

    animal4 = Fabric(animal_class='fish', kind='Плотва', name='Сара', age=0.5, size=11)
    print(animal4.get_info().get_animal_info())