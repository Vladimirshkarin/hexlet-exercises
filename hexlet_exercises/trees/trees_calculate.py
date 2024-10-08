# url: https://ru.hexlet.io/courses/python-trees/lessons/calculate/
# exercise_unit
#
#
# В Linux, MacOS и многих операционных системах существует утилита du.
# Она умеет подсчитывать, сколько места занимают указанные файлы и директории.
# Например, так:
#
#  tmp$ du -sh *
#  97k	.venv
#   0B	com.docker.vmnetd.socket
#  10M	credo
# 4.0K	debug.mjs
#   0B	filesystemui.socket
# 4.0K	index.py
#  88K	poetry-lock.json
#  22M	taxdome
# Перед решением этого задания обязательно попрактикуйтесь с этой утилитой в
# терминале, посмотрите ее опции через man du. Экспериментировать нужно в
# локально установленной операционной системе.

# solution.py
# Реализуйте функцию du. Она должна принимать на вход директорию и возвращать:

# Список всех директорий и файлов, которые вложены в указанную директорию на
# один уровень
# Размер всей директории, который складывается из сумм всех размеров файлов,
# находящихся внутри во всех подпапках
# Так это выглядит в коде:

# from hexlet.fs import mkdir, mkfile
# from solution import du
# tree = mkdir('/', [
#     mkdir('etc', [
#         mkdir('apache'),
#         mkdir('nginx', [
#             mkfile('nginx.conf', {'size': 800}),
#         ]),
#         mkdir('consul', [
#             mkfile('.config.json', {'size': 1200}),
#             mkfile('data', {'size': 8200}),
#             mkfile('raft', {'size': 80}),
#         ]),
#     ]),
#     mkfile('hosts', {'size': 3500}),
#     mkfile('resolve', {'size': 1000}),
# ])
# du(tree)  # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
# Примечания
# Размер файла задается в метаданных, при этом сами папки размера не имеют
# В структуре результирующего списка каждый элемент является кортежем с двумя
# значениями — именем директории и размером файлов внутри
# Результат отсортирован по размеру в обратном порядке — сверху тяжелые, снизу
# легкие
# Подсказки
# sort
from hexlet.fs import get_children, get_meta, get_name, is_file


# BEGIN (write your solution here)
def get_files_size(node):
    if is_file(node):
        return int(get_meta(node).get("size"))
    children = get_children(node)
    descendant_size = list(map(get_files_size, children))
    return sum(descendant_size)


def du(node):
    children = get_children(node)
    result = list(
        map(
            lambda child: (get_name(child), get_files_size(child)),
            children,
        )
    )
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
    return sorted_result
# END


# BEGIN reference solution
def calculate_entry_size(tree):
    if is_file(tree):
        meta = get_meta(tree)
        return meta["size"]
    children = get_children(tree)
    sizes = list(map(calculate_entry_size, children))
    return sum(sizes)


def du_ref(tree):
    children = get_children(tree)
    result = list(
        map(
            lambda child: (get_name(child), calculate_entry_size(child)),
            children,
        )
    )
    result.sort(key=lambda entry: entry[1], reverse=True)
    return result
# END reference solution
