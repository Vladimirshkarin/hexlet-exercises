from hexlet_exercises.oop_basics.oop_inheritance import Counter, LimitedCounter


def test_counter():
    counter = Counter()
    counter.inc()
    counter.inc(7)
    assert counter.value == 8
    counter.dec(10)
    assert counter.value == 0
    counter.inc(7)
    counter.inc(7)
    assert counter.value == 14


def test_limitedcounter():
    counter = LimitedCounter(limit=10)
    counter.inc()
    counter.inc(7)
    assert counter.value == 8
    counter.dec(10)
    assert counter.value == 0
    counter.inc(7)
    counter.inc(7)
    assert counter.value == 10


