from hexlet_exercises.oop_design.configuration_setters import Truncater


def test_truncate():
    truncater = Truncater()
    assert truncater.truncate("one two") == "one two"
    assert truncater.truncate("one two", length=6) == "one tw..."
    assert truncater.truncate("one two", separator=".") == "one two"
    assert truncater.truncate("one two", length=3) == "one..."

    truncater = Truncater(length=3)
    assert truncater.truncate("one two") == "one..."
    assert truncater.truncate("one two", separator="!") == "one!"
    assert truncater.truncate("one two") == "one..."

    assert truncater.truncate("one two", length=7) == "one two"
