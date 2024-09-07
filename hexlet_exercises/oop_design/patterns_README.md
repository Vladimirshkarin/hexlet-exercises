url: https://ru.hexlet.io/courses/python-object-oriented-design/lessons/patterns/exercise_unit

Реализуйте функцию to_Klass(), которая принимает на вход словарь и возвращает
объект типа Klass такой же структуры.

data = {
    'key': 'value',
    'key2': 'value2',
}
config = to_Klass(data)

config.key ## value
config.key2 ## value2
Подсказки
Вам понадобится функция setattr
user = User()
setattr(user, 'f', 'foo')
print(user.f) #=> foo
В пайтоне классы созданные лишь для хранения значений принято оборачивать в
декоратор @dataclass
А чтобы не конфликтовать с зарезервированным именем class принято именовать
через k
