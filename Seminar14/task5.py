# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта. Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
#
# Метод входа в систему – требует указать имя и id пользователя.
# Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта.
# Если в списке его нет, то вызывается исключение доступа.
# Если пользователь присутствует в списке пользователей проекта, то пользователь, который входит получает его уровень доступа и становится администратором.
#
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.

# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
import json
from task3_4 import User
from exceptions import NotAllowedError, LevelError, AdminNotFoundError


class Project:
    """Класс управления пользователями проекта"""

    def __init__(self, project_users=None):
        self.project_users = project_users or []
        self.admin = None

    @classmethod
    def fill_project_users(cls, path):
        """Метод, заполняющий список пользователей проекта из json файла"""
        with open(path, "r", encoding="utf-8") as j:
            file = json.load(j)
            temp = []
            for key in file:
                for user in file[key].items():
                    temp.append(User(user[1], int(user[0]), int(key)))
            return cls(temp)

    def enter(self, name, id_):
        """
        Метод входа в систему.
        :param name: Имя пользователя
        :param id_: Идентификатор пользователя
        :exception NotAllowedError: Срабатывает, если пользователя нет в списке.
        """
        user = User(name, id_)
        for proj_user in self.project_users:
            if user == proj_user:
                self.admin = proj_user
                break
        else:
            raise NotAllowedError(name, id_)

    def add_user(self, name, id_, level):
        """
        Метод добавления нового пользователя в проект.
        :param name: Имя пользователя
        :param id_: Идентификатор пользователя
        :param level: Уровень доступа пользователя
        :exception AdminNotFoundError: Срабатывает, если не установлен администратор.
        :exception LevelError: Срабатывает, если уровень пользователя больше, чем у администратора
        """
        if self.admin is None:
            raise AdminNotFoundError
        if level < self.admin.level:
            raise LevelError(level, self.admin.level)
        self.project_users.append(User(name, id_, level))

    def del_user(self, name, id_, level):
        """
        Метод удаления пользователя из проекта.
        :param name: Имя пользователя
        :param id_: Идентификатор пользователя
        :param level: Уровень доступа пользователя
        :exception AdminNotFoundError: Срабатывает, если не установлен администратор.
        :exception LevelError: Срабатывает, если уровень пользователя больше, чем у администратора
        :exception ValueError: Срабатывает, если пользователя с введёнными данными нет в проекте
        """
        if self.admin is None:
            raise AdminNotFoundError()
        if level < self.admin.level:
            raise LevelError(level, self.admin.level)
        try:
            self.project_users.remove(User(name, id_, level))
        except ValueError:
            print(f"Ошибка удаления!\nПользователя {name} нет в списке пользователей!")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Метод выхода из контекстного менеджера
        При выходе, актуальный список пользователей сохраняется в файл.
        """
        self.file = open(f'project_users.json', 'w', encoding='utf-8')
        temp = {k: {} for k in range(1, 8)}
        for user in self.project_users:
            temp[user.level].update({user.id_: user.name})
        json.dump(temp, self.file, ensure_ascii=False)
        self.file.close()

    def __eq__(self, other):
        return self.project_users == other.project_users


if __name__ == '__main__':
    with Project().fill_project_users() as p:
        print(p.project_users)
        p.enter("Григорий", 654)
        print(p.admin)
        # p.del_user("Григорий", 444, 5)