# ulr: https://ru.hexlet.io/courses/python-trees/lessons/accumulator/
# exercise_unit
#
#
# Реализуйте функцию find_files_by_name(). Она должна принимать на вход
# файловое дерево и подстроку, а затем возвращать список файлов, имена которых
# содержат эту подстроку. Функция должна вернуть полные пути файлам:
#
# from hexlet.fs import mkdir, mkfile
# from solution import find_files_by_name
# tree = mkdir('/', [
#     mkdir('etc', [
#         mkdir('apache'),
#         mkdir('nginx', [
#             mkfile('nginx.conf', {'size': 800}),
#         ]),
#         mkdir('consul', [
#             mkfile('config.json'),
#             mkfile('data'),
#             mkfile('raft'),
#         ]),
#     ]),
#     mkfile('hosts', {'size': 3500}),
#     mkfile('resolve', {'size': 1000}),
# ])
# find_files_by_name(tree, 'co')
# # ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
# Подсказки
# Для реализации этой логики вам понадобится аккумулятор, в котором будет
# храниться путь от корня до текущего узла. При проваливании внутрь директорий к нему добавляется имя текущей директории. В остальном логика работы идентична примеру из теории
# Переменную с путем от корня до текущего узла можно назвать ancestry
# Для построения путей используйте функцию os.path.join()

import os

from hexlet.fs import flatten, get_children, get_name, is_file


# BEGIN (write your solution here)

# END


# BEGIN reference solution

# END reference solution
