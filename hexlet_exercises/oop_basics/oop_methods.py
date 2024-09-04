# url: https://ru.hexlet.io/courses/python-oop-basics/lessons/methods/
# exercise_unit

# Реализуйте класс Counter, представляющий собой счётчик, хранящий
# неотрицательное целочисленное значение и позволяющий это значение изменять:

# атрибут value должен хранить текущее значение счётчика (вначале равное нулю)
# метод inc() должен увеличивать текущее значение на delta единиц (на 1 по
# умолчанию)
# метод dec() должен уменьшать текущее значение на delta единиц (на 1 по
# умолчанию). Если значение delta больше текущего значения счетчика, текущее
# значение должно стать равным нулю, так как счетчик хранит неотрицательные
# значения
# c = Counter()
# c.inc()
# c.inc()
# c.inc(40)
# c.value  # 42
# c.dec()
# c.dec(30)
# c.value  # 11
# # Счетчик не должен уходить в отрицательные значения
# c.dec(delta=100)
# c.value  # 0

# BEGIN (write your solution here)
class Counter:
    value = 0

    def inc(self, delta=1):
        self.value += delta

    def dec(self, delta=1):
        self.value = max(0, self.value - delta)
# END


# BEGIN reference solution
class Counter_ref:
    value = 0

    def inc(self, delta=1):
        self.value = max(self.value + delta, 0)

    def dec(self, delta=1):
        self.inc(-delta)
# END reference solution
