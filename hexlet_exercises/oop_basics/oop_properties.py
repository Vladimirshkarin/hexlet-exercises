# url: https://ru.hexlet.io/courses/python-oop-basics/lessons/properties/
# exercise_unit

# Реализуйте класс HourClock, который будет изображать часы с одной лишь
# часовой стрелкой. Текущее время (час) должно сообщать свойство hours. Это же
# свойство должно позволять изменять положение часовой стрелки (посредством
# сеттера). При изменении положения стрелки нужно контролировать, чтобы
# значение оставалось в диапазоне 0..11 (часов).

# clock = HourClock()
# clock.hours  # 0
# # в начале часовая стрелка всегда на нуле
# clock.hours += 5
# # ^ эквивалентно clock.hours = clock.hours + 5
# clock.hours += 5
# clock.hours  # 10
# clock.hours += 5
# clock.hours  # 3
# clock.hours -= 4
# clock.hours  # 11
# clock.hours = 123
# clock.hours  # 3
# Подсказки
# Используйте модульную арифметику


# BEGIN (write your solution here)
class HourClock:
    def __init__(self, _hours=0):
        self._hours = 0

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, new):
        self._hours = new % 12
# END


# BEGIN reference solution
class HourClock_ref:
    def __init__(self):
        """Create a new hour clock."""
        self.hand_position = 0

    @property
    def hours(self):
        return self.hand_position

    @hours.setter
    def hours(self, new_position):
        self.hand_position = new_position % 12
# END reference solution
