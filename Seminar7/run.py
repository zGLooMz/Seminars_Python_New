from task_1 import generate_files
from task_2 import sort_files_by_folders
from task_3 import group_renaming

if __name__ == '__main__':
    # Генерируем файлы
    generate_files('.mp3', dir='./Files', min_size=5, max_size=10, file_count=10)
    generate_files('.mp4', dir='./Files', min_size=5, max_size=10, file_count=10)
    generate_files('.wav', dir='./Files', min_size=5, max_size=10, file_count=10)
    generate_files('.jpg', dir='./Files', min_size=5, max_size=10, file_count=10)
    generate_files('.gif', dir='./Files', min_size=5, max_size=10, file_count=10)
    generate_files('.doc', dir='./Files', min_size=5, max_size=10, file_count=10)
    generate_files('.pdf', dir='./Files', min_size=5, max_size=10, file_count=10)
    generate_files('.zip', dir='./Files', min_size=5, max_size=10, file_count=10)

    # Раскидываем файлы по папкам
    sort_files_by_folders('./Files')

    # Групповое переименование файлов
    group_renaming('./Files/', '.zip', 'renamed',
                   '.rar', 2, (1, 3))