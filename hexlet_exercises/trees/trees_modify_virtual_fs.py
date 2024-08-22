# Реализуйте функцию compress_images(). Она должна принимать на вход
# директорию, находить внутри нее картинки и уменьшать
# свойство size в их метаданных в два
# раза. Функция должна вернуть обновленную директорию со сжатыми картинками и
# всеми остальными данными, которые были внутри этой директории.

# Картинками считаются все файлы, заканчивающиеся на .jpg:

# from hexlet.fs import mkdir, mkfile
# from solution import compress_images
# tree = mkdir(
#     'my documents',
#     [
#         mkfile('avatar.jpg', {'size': 100}),
#         mkfile('photo.jpg', {'size': 150}),
#     ],
#     {'hide': False}
# )
# compress_images(tree)
# # {
# #     'name': 'my documents',
# #     'type': 'directory',
# #     'children': [
# #         {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
# #         {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
# #     ],
# #     'meta': {'hide': False},
# # }

import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)

# END
