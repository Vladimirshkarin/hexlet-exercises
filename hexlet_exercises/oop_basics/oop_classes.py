# url: https://ru.hexlet.io/courses/python-oop-basics/lessons/classes
# /exercise_unit

# Вам нужно реализовать класс Color, который должен содержать атрибуты red,
# green и blue. Значениями этих атрибутов должны быть представления цвета в
# цветовой модели RGB. Для получения значений для атрибутов используйте
# предоставленную функцию rgb.
# from solution import Color, rgb
# Color.red  # (255, 0, 0)
# Color.green == rgb(0, 255, 0)  # True


def rgb(red, green, blue):
    return red, green, blue


# BEGIN (write your solution here)
class Color:
    red = rgb(255, 0, 0)
    green = rgb(0, 255, 0)
    blue = rgb(0, 0, 255)
# END


# BEGIN reference solution
class ColorRef:
    red = rgb(255, 0, 0)
    green = rgb(0, 255, 0)
    blue = rgb(0, 0, 255)
# END reference solution
