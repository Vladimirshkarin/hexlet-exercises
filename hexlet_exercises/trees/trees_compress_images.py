# url: https://ru.hexlet.io/courses/python-trees/lessons/
# manipulations/exercise_unit
#
#
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
def change_meta(node):
    name = get_name(node)
    new_meta = copy.deepcopy(get_meta(node))
    if name.endswith(".jpg") and isinstance(
                                            new_meta.get("size"), (int, float)
                                            ):
        new_meta["size"] = new_meta["size"] // 2
    if is_file(node):
        return mkfile(name, new_meta)
    return mkdir(name, get_children(node), new_meta)


def compress_images(tree):
    children = get_children(tree)
    new_children = list(map(change_meta, children))
    new_meta = copy.deepcopy(get_meta(tree))
    new_tree = mkdir(get_name(tree), new_children, new_meta)
    return new_tree
# END


# BEGIN reference solution
def compress_images_ref(tree):
    children = get_children(tree)

    def reduce_image_size(node):
        name = get_name(node)
        if not is_file(node) or not name.endswith(".jpg"):
            return node
        meta = get_meta(node)
        new_meta = copy.deepcopy(meta)
        new_meta["size"] //= 2
        return mkfile(name, new_meta)

    new_children = map(reduce_image_size, children)
    new_meta = copy.deepcopy(get_meta(tree))
    return mkdir(get_name(tree), list(new_children), new_meta)
# END reference solution
