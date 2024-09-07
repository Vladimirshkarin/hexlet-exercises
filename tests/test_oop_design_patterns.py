from hexlet_exercises.oop_design.patterns import to_Klass
from hexlet_exercises.oop_design.patterns import Klass


def test_same_type():
    std = to_Klass({})
    assert type(std) == Klass  # noqa: E721


def test_to_Klass():
    data = {"key": "value", "key2": "value2"}
    std = to_Klass(data)
    assert std.key == "value"
    assert std.key2 == "value2"

    data2 = {"keysdd": "vasdfalue", "kasdfey2": "asdvalue2"}
    std = to_Klass(data2)
    assert std.keysdd == "vasdfalue"
    assert std.kasdfey2 == "asdvalue2"
