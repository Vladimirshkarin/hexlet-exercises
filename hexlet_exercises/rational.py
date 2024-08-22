# src/rational.py
# Реализуйте абстракцию для работы с рациональными числами
# , которая включает в себя следующие функции:
# Конструктор make — принимает на вход числитель и знаменатель
# , возвращает дробь
# Селектор get_numer — возвращает числитель
# Селектор get_denom — возвращает знаменатель
# Сложение add — складывает переданные дроби
# Вычитание sub — находит разность между двумя дробями
# Не забудьте реализовать нормализацию дробей
# удобным для вас способом.

# Примеры работы:

# import rational

# rat1 = rational.make(3, 9)
# rational.get_numer(rat1)  # 1
# rational.get_denom(rat1)  # 3
# rat2 = rational.make(10, 3)
# rat3 = rational.add(rat1, rat2)
# rational.to_str(rat3)  # 11/3
# rat4 = rational.sub(rat1, rat2)
# rational.to_str(rat4)  # -3/1
# Подсказки
# Приведение дробей к единому знаменателю
# Функция gcd из модуля math находит наибольший
# общий делитель двух чисел
# Функция to_str возвращает строковое
# представление числа (используется для отладки)
# Функция int преобразует значение к целому числу
import math


# BEGIN (write your solution here)
def make(numer, denom):
    gcd = math.gcd(int(numer), int(denom))
    normalized_numer = numer // gcd
    normalized_denom = denom // gcd
    return {'numer': normalized_numer, 'denom': normalized_denom}


def get_numer(rat):
    return rat['numer']


def get_denom(rat):
    return rat['denom']


def add(rat1, rat2):
    gcd = math.gcd(get_numer(rat1), get_numer(rat2))
    lcm = (get_denom(rat1) * get_denom(rat2)) // gcd
    numer1 = get_numer(rat1) * lcm // get_denom(rat1)
    numer2 = get_numer(rat2) * lcm // get_denom(rat2)
    result_numer = numer1 + numer2
    return make(result_numer, lcm)


def sub(rat1, rat2):
    gcd = math.gcd(get_numer(rat1), get_numer(rat2))
    lcm = (get_denom(rat1) * get_denom(rat2)) // gcd
    numer1 = get_numer(rat1) * lcm // get_denom(rat1)
    numer2 = get_numer(rat2) * lcm // get_denom(rat2)
    result_numer = numer1 - numer2
    return make(result_numer, lcm)
# END


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"


# BEGIN reference solution
def make_ref(numer, denom):
    gcd = math.gcd(int(numer), int(denom))
    return {'numer': numer // gcd, 'denom': denom // gcd}


def get_numer_ref(rat):
    return rat['numer']


def get_denom_ref(rat):
    return rat['denom']


def add_ref(rat1, rat2):
    first_numer = get_numer_ref(rat1)
    second_numer = get_numer_ref(rat2)
    first_denom = get_denom_ref(rat1)
    second_denom = get_denom_ref(rat2)
    return make_ref(first_numer * second_denom + second_numer * first_denom,
                    first_denom * second_denom,
                    )


def sub_ref(rat1, rat2):
    first_numer = get_numer_ref(rat1)
    second_numer = get_numer_ref(rat2)
    first_denom = get_denom_ref(rat1)
    second_denom = get_denom_ref(rat2)
    return make_ref(first_numer * second_denom - second_numer * first_denom,
                    first_denom * second_denom,
                    )
# END reference solution
