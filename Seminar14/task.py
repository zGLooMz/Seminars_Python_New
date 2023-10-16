# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import json
import pytest

from task5 import Project
from task3_4 import User
from exceptions import NotAllowedError, AdminNotFoundError, LevelError


@pytest.fixture
def get_file(tmp_path):
    f_name = tmp_path / 'test_file.json'
    with open(f_name, 'w', encoding='utf-8') as f:
        data = {
            "1": {"741": "Наталья", },
            "2": {"456": "Антон", },
            "3": {
                "789": "Александр",
                "852": "Михаил",
            },
            "5": {"654": "Григорий", },
            "7": {"147": "Сергей", }
        }

        json.dump(data, f, ensure_ascii=True)
    return f_name


@pytest.fixture
def fill_users(get_file):
    proj = Project().fill_project_users(get_file)
    return proj


def test_fill_users(get_file, fill_users):
    p = Project().fill_project_users(get_file)
    assert fill_users == p


@pytest.mark.parametrize("name, id_, result",
                         [
                             ("Григорий", 654, User("Григорий", 654)),
                             ("Иван", 777, "Отказано в доступе!\nПользователь Иван/777 не найден."),
                             ("Наталья", 741, User("Наталья", 741)),
                         ]
                         )
def test_enter(name, id_, result, fill_users):
    if isinstance(result, User):
        fill_users.enter(name, id_)
        assert fill_users.admin == result
    else:
        with pytest.raises(NotAllowedError) as exc_info:
            fill_users.enter(name, id_)
        assert str(exc_info.value) == result


@pytest.mark.parametrize("name, id_, level, result, exc",
                         [
                             ("Иван", 777, 6, User("Иван", 777, 6), None),
                             ("Иван", 777, 6,
                              "Отказано в доступе!\nАдминистратор не найден!\nИспользуйте команду 'enter' для входа в систему.",
                              AdminNotFoundError),
                             ("Иван", 777, 2,
                              "Отказано в доступе!\nВаш уровень доступа(2) должен быть ниже чем, уровень доступа администратора(5)",
                              LevelError),
                         ])
def test_add_user(name, id_, level, result, exc, fill_users):
    if exc is None:
        fill_users.enter("Григорий", 654)
        fill_users.add_user(name, id_, level)
        assert result in fill_users.project_users
    elif exc == AdminNotFoundError:
        with pytest.raises(AdminNotFoundError) as exc_info:
            fill_users.add_user(name, id_, level)
        assert str(exc_info.value) == result
    elif exc == LevelError:
        with pytest.raises(LevelError) as exc_info:
            fill_users.enter("Григорий", 654)
            fill_users.add_user(name, id_, level)
        assert str(exc_info.value) == result


@pytest.mark.parametrize("first_user, second_user, exp",
                         [
                             (User("Иван", 123), User("Иван", 123), True),
                             (User("Михаил", 123), User("Иван", 123), False),
                         ])
def test_users(first_user, second_user, exp):
    assert (first_user == second_user) == exp


if __name__ == "__main__":
    pytest.main(["-v"])