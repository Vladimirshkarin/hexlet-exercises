# url: https://ru.hexlet.io/courses/python-trees/lessons/definition/
# exercise_unit
#
#
# В этом задании под деревом понимается любой список элементов,
# которые в свою очередь могут быть также деревьями или списками. Например:
#
# [
#   3, # Лист
#   [5, 3], # Узел
#   [[2]] # Узел
# ]
# Больше примеров вы можете найти в тестах.
#
# solution.py
# Реализуйте функцию remove_first_level(). Она должна принимать на вход
# дерево и возвращать новое дерево, элементами которого являются потомки
# вложенных узлов:
#
# from solution import remove_first_level
#
# tree1 = [[5], 1, [3, 4]]
# remove_first_level(tree1)  # [5, 3, 4]
# tree2 = [1, 2, [3, 5], [[4, 3], 2]]
# remove_first_level(tree2)  # [3, 5, [4, 3], 2]
# Подсказки
# Подключенный в модуле пакет itertools можно использовать, но это
# необязательно
import itertools


# BEGIN (write your solution here)
def remove_first_level(tree):
    result = filter(lambda item: isinstance(item, list), tree)
    return list(itertools.chain(*result))
# END


# BEGIN (write your solution here)
def remove_first_level_old(tree):
    result = []
    for item in tree:
        if type(item) is list:
            for value in item:
                result.append(value)
    return result
# END


# BEGIN reference solution
def remove_first_level_ref(tree):
    children = filter(lambda item: isinstance(item, list), tree)
    return list(itertools.chain(*children))
# END reference solution
