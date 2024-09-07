from hexlet_exercises.oop_basics.oop_exceptions import suppress


def walk(path, structure):
    """Walk down to structure using path."""
    if not path:
        return structure
    key, *rest_path = path
    return walk(rest_path, structure[key])


def test_walk():
    assert walk([0], "Cat") == "C"
    assert walk(["a", 1], {"a": ("foo", "bar")}) == "bar"
    assert walk(["x", 1, 0], {"x": ("foo", "bar")}) == "b"


def test_suppress():
    @suppress(ZeroDivisionError, or_return=0)
    def safe_div(a, *, b):
        return a // b

    assert safe_div(10, b=3) == 3
    assert safe_div(10, b=0) == 0


def test_suppress_walk():
    safe_walk = suppress((KeyError, IndexError))(walk)

    assert safe_walk([1], "") is None
    assert safe_walk(["a"], {}) is None
    assert safe_walk([0, 0, 1], (("?", 100), 200)) is None
