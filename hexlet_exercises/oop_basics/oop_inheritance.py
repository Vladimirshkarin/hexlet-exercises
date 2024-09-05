# url: https://ru.hexlet.io/courses/python-oop-basics/lessons/inheritance/
# exercise_unit

# Вам дан класс Counter, реализующий счетчик с инкрементом и декрементом. Вам
# нужно реализовать класс-потомок LimitedCounter, который будет отличаться от
# Counter тем, что при инициализации будет принимать в качестве аргумента лимит
# — максимальное возможное значение счетчика.

# Требования к классу LimitedCounter:

# Класс должен максимально использовать методы предка, если таковые
# переопределяет
# Минимальное значение счетчика Counter — 0, должно оставаться таковым и для
# LimitedCounter
# counter = LimitedCounter(limit=10)
# counter.inc()
# counter.inc(7)
# counter.value  # 8
# counter.dec(10)
# counter.value  # 0
# counter.inc(7)
# counter.inc(7)
# counter.value  # 10
# Подсказки
# Задание можно решить разными способами. Нет единственного верного решения.
# Так что творите!


class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


# BEGIN (write your solution here)

# END


# BEGIN reference solution

# END reference solution
