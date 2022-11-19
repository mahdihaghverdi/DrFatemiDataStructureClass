from dsp import Stack


def test_initializing():
    _ = Stack()
    assert not _._stack


def test_init__bool__():
    _ = Stack()
    assert not _


def test_init_iter():
    _ = Stack(range(10))
    assert _._stack


def test_pop():
    _ = Stack(range(10))
    for __ in reversed(range(10)):
        assert _.pop() == __


def test_append():
    _ = Stack()
    for num in range(10):
        _.append(num)

    for num in reversed(range(10)):
        assert _.pop() == num


def test__len__():
    _ = Stack()
    assert not len(_)

    _ = Stack(range(10))
    assert len(_) == 10


def test__contains__():
    _ = Stack(range(10))
    assert 10 not in _
    assert 9 in _


def test__iter__():
    _ = Stack(range(10))
    assert list(_) == list(reversed(range(10)))
    assert _._stack == list(reversed(range(10)))
