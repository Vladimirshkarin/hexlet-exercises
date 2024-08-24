# url: https://ru.hexlet.io/courses/python-trees/lessons/traversal
# /exercise_unit

# Реализуйте функцию downcase_file_names(). Она должна принимать на вход
#  директорию (объект-дерево) и приводить имена всех файлов к нижнему регистру,
#  причем в корневой директории и во всех вложенных. Функция должна возвращать
# результат в виде обработанной директории:

# from hexlet.fs import mkdir, mkfile, get_children, get_name
# from solution import downcase_file_names
# tree = mkdir('/', [
#     mkdir('eTc', [
#         mkdir('NgiNx', [], {'size': 4000}),
#         mkdir(
#             'CONSUL',
#             [mkfile('config.JSON', {'uid': 0})],
#         ),
#     ]),
#     mkfile('HOSTS'),
# ])
# new_tree = downcase_file_names(tree)
# new_file = get_children(new_tree)[1]
# get_name(new_file)  # hosts
# Подсказки
# Придерживайтесь идеи иммутабельности - функция должна возвращать новое дерево
# , значит его метаданные должны быть скопированны (deep copy), а не ссылаться
#  на оригинальные

import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)
def downcase_file_names(node):
    name = get_name(node)
    new_meta = copy.deepcopy(get_meta(node))
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    else:
        children = get_children(node)
        new_children = list(map(downcase_file_names, children))
        return mkdir(name, new_children, new_meta)
# END


# BEGIN reference solution
def downcase_file_name_ref(node):
    new_meta = copy.deepcopy(get_meta(node))
    name = get_name(node)
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    children = get_children(node)
    new_children = map(downcase_file_names, children)
    return mkdir(name, list(new_children), new_meta)
# END reference solution
