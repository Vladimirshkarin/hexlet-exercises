url: https://ru.hexlet.io/courses/python-object-oriented-design/lessons/fluent-interface/exercise_unit

Эту задачу можно решить огромным числом способов. Почти наверняка ваш способ будет не такой как решение учителя. Для отработки fluent interface в задаче используется класс Collection. Мы не даем никаких подсказок насчет того, какие функции нужно использовать. Как минимум вы знаете главную тройку map, filter и reduce. Их вполне достаточно, но можно и лучше если внимательно поизучать функции в модуле сollection.py.

data = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 20}, {'name': 'Charlie', 'age': 30}]
c = Collection(data)
c.unique().all()

# [{'age': 30, 'name': 'Charlie'},
# {'age': 20, 'name': 'Bob'},
# {'age': 20, 'name': 'Alice'}]

c.unique().group_by(lambda row: (row['age'], row['name'])).all()
# [{30: ['Charlie']}, {20: ['Bob', 'Alice']}]

c.unique().group_by(lambda row: (row['age'], row['name'])).sort_by(lambda row: list(row.keys())).all()
# [{20: ['Bob', 'Alice']}, {30: ['Charlie']}]
solution.py
Реализуйте функцию format() которая принимает на вход список городов, производит внутри некоторые преобразования и возвращает структуру определенного формата.

Входные данные

raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]
Входная структура представляет из себя список городов, где каждый город это словарь с ключами name и country. Значения в этих ключах не нормализованы. Они могут быть в любом регистре и содержать начальные и концевые пробелы. Сами города могут дублироваться в рамках одной страны.

Результат

expected = [{'russia': ['moscow', 'samara']},
            {'turkey': ['antalia', 'istambul']},]
Конечная структура — словарь, в котором ключ это страна, а значение — список имен городов отсортированный по именам. Сама структура отсортирована по странам. Дублей городов в выходной структуре быть не должно, а сами страны и города должны быть записаны в нижнем регистре без ведущих и концевых пробелов.

Подсказки
для вывода промежуточных значений используйте метод .print()
