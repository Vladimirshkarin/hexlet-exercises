В данном упражнении вам предстоит реализовать класс Url, который позволяет извлекать из HTTP адреса, представленного строкой, его части.

Класс должен содержать методы:

__init__ — принимает на вход HTTP адрес в виде строки.

get_scheme() — возвращает протокол передачи данных.

get_hostname() — возвращает имя хоста.

get_query_params() — возвращает параметры запроса в виде пар ключ-значение объекта.

get_query_param() — получает значение параметра запроса по имени. Если параметр с переданным именем не существует, метод возвращает значение заданное вторым параметром (по умолчанию равно None).

__eq__(self, other) — сравнивает два объекта класса Url и возвращает результат сравнения — True или False.

url = Url('http://hexlet.io:80?key=value&key2=value2')
url.get_scheme() # http
url.get_hostname() # hexlet.io
url.get_query_params()
# {
#  key: [value],
#  key2: [value2],
# }
url.get_query_param('key') # value
# второй параметр — значение по умолчанию
url.get_query_param('key2', 'lala') # value2
url.get_query_param('new', 'ehu') # ehu
url.get_query_param('new') # None
url == Url('http://hexlet.io:80?key=value&key2=value2') # True
url == Url('http://hexlet.io:80?key=value') # False
Подсказки
для парсинга url воспользуйтесь функциями urlparse и parse_qs из модуля urllib
__eq__
