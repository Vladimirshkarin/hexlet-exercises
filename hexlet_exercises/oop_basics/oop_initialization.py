# url: https://ru.hexlet.io/courses/python-oop-basics/lessons/initialization/
# exercise_unit

# Вам предстоит снова реализовать класс Counter. Но на этот раз счётчик будет
# иммутабельным и всё ещё неотрицательным целочисленным. Методы inc() и dec()
# должны возвращать новый счётчик с изменённым в большую или соответственно
# меньшую сторону значением value (по умолчанию счётчик изменяется на единицу).

# c = Counter()
# c.inc()  # возвращает новый объект класса
# c.inc().value  # возвращает value нового объекта
# В этой реализации вам нужно объявить в классе функцию-инициализатор,
# позволяющую задать начальное значение счётчика (атрибут value). Если же
# значение при инстанциировании не будет задано, следует принять его по
# умолчанию равным нулю.

# Атрибут value первоначального объекта после применения методов должен всё
# ещё содержать неизменное значение. Неизменность старого объекта и является
# условием иммутабильности.

# c = Counter()
# c.inc().inc(5).dec(2).value  # 4

# # Старый экземпляр не должен изменяться
# d = c.inc(100)
# d.dec().value  # 99

# forty_two = Counter(42)
# forty_two.value  # 42
# Внимание! В самом классе атрибут value не должен быть объявлен. Этот атрибут
# должен добавляться в объект только в инициализаторе.


# BEGIN (write your solution here)
class Counter:
    def __init__(self, value=0):
        if value < 0:
            self.value = 0
        else:
            self.value = value

    def inc(self, delta=1):
        return Counter(max(self.value + delta, 0))

    def dec(self, delta=1):
        return Counter(max(0, self.value - delta))


# END


# BEGIN reference solution
class Counter_ref:
    def __init__(self, value=0):
        """Create an immutable counter."""
        self.value = max(value, 0)

    def inc(self, delta=1):
        return Counter(self.value + delta)

    def dec(self, delta=1):
        return self.inc(-delta)
# END reference solution
