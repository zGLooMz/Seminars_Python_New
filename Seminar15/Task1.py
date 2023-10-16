# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
import logging
from collections import namedtuple
from pathlib import Path

logging.basicConfig(filename='path_data.log', level=logging.INFO,
                    format='{levelname}>>>  {msg} (time {asctime})', style='{', datefmt='%d-%m-%Y %H:%M:%S')
logger = logging.getLogger(__name__)

PathData = namedtuple('PathData', ['name', 'extension', 'is_dir', 'parent_dir'])


def get_path_data(path):
    for item in Path(path).iterdir():
        if item.is_file() and not Path(item).suffix == '.pyc':
            name, extension = item.name.split('.')
            path_data = PathData(name, '.' + extension, False, item.parent.name)
            logging.info(path_data)
        elif item.is_dir():
            path_data = PathData(item.name, None, True, item.parent.name)
            logging.info(path_data)
            get_path_data(str(item))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-my_path', metavar='my_path', type=str, help='Input path to scanning Directory',
                        default='../Seminar6')
    args = parser.parse_args()
    print(get_path_data(args.my_path))

# Запускаю скрипт через терминал:
# python Seminars_Python_New\Seminar15\Task1.py -my_path 'H:\PythonNew\Seminars_Python_New\Seminar6'