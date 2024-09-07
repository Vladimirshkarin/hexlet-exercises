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

from functools import wraps


# BEGIN (write your solution here)
def suppress(types_of_error, or_return=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except types_of_error:
                return or_return

        return inner

    return wrapper
# END


# BEGIN reference solution
def suppress_(exception, *, or_return=None):
    """Suppress exceptions of provided class(es) and return a value instead."""

    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exception:
                return or_return

        return inner

    return wrapper
# END reference solution
