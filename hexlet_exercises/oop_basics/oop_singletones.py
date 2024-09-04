# url: https://ru.hexlet.io/courses/python-oop-basics/lessons/singletones
# /exercise_unit

# В этой практике вы увидите одно из применений глобального изменяемого
# состояния (когда таковое всё же применяют): глобальный реестр классов.
# Этот реестр позволяет зарегистрировать некие классы в одном месте программы,
# а потом получить доступ ко всем зарегистрированным классам в любом участке
# кода.

# src/registry.py
# В этом модуле находится реализация глобального реестра классов. В этот
# реестр любой класс можно добавить с помощью функции registry.add, а уже
# зарегистрированные классы можно всегда найти в словаре registry.CLASSES.
# Выглядит использование реестра так:

# import registry
# class Foo:
#     pass

# registry.add(Foo)
# registry.CLASSES  # {'__main__.Foo': <class '__main__.Foo'>}
# Обязательно посмотрите содержимое модуля src/registry.py — это может быть
# интересно!

# src/solution.py
# Здесь вы найдёте объявление двух классов: Cat и Bird. Вам нужно
# зарегистрировать оба этих класса в реестре. Тесты будут проверять, что
# классы успешно зарегистрированы.


class Cat:
    legs = 4


class Bird:
    legs = 2


# BEGIN (write your solution here)
import registry  # noqa: E402

registry.add(Cat)
registry.add(Bird)
# END


# BEGIN reference solution
# Same
# END reference solution
