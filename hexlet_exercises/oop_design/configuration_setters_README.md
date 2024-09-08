url: https://ru.hexlet.io/courses/python-object-oriented-design/lessons/configuration-setters/exercise_unit

Для работы с текстом в вебе бывает полезна функция truncate(), которая обрезает слишком длинный текст и ставит в конце, например, многоточие:

truncate('long text', {'length': 3})  ## lon...
solution.py
Реализуйте класс Truncater с единственным методом truncate(). В классе уже присутствует конфигурация по умолчанию:

OPTIONS = {
    'separator': '...',
    'length': 200,
}
separator отвечает за символ(ы) добавляющиеся в конце, после обрезания строки, а length это длина до которой происходит сокращение. Если строка короче или равна этой опции, то никакого сокращения не происходит. Конфигурацию по умолчанию можно переопределить передав новую при инициализации (она мержится с тем что в классе), а также через передачу конфигурации вторым параметром в метод truncate(). Оба этих способа можно комбинировать.

truncater = Truncater()

truncater.truncate('one two')  # one two

truncater.truncate('one two', length=6)  # one tw...

truncater2 = Truncater(length=6, separator='*')
truncater2.truncate('one two')  # one tw*
