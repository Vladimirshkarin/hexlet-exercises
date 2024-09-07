# url: https://ru.hexlet.io/courses/python-oop-basics/lessons/exceptions/
# exercise_unit
# Реализуйте декоратор suppress ("подавлять"), который должен перехватывать
# заданное исключение (одно или кортеж), если таковое возникнет при вызове
# оборачиваемой функции, и возвращать вместо ошибки заданное значение (keyword
# -only аргумент "or_return", значение по умолчанию — None).

# @suppress(ZeroDivisionError, or_return=42)
# def foo():
#      return 1 // 0

# foo()  # 42

# @suppress((KeyError, IndexError))
# def get_item(key, structure):
#      return structure[key]

# get_item(7, "foo") is None  # True
# get_item('a', {}) is None  # True
