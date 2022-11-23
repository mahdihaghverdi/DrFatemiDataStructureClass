from dsp import MySpecialQueue


def test_appendmiddle():
    _ = MySpecialQueue(range(1, 5))
    _.appendmiddle(0)
    _iter = iter(_)
    next(_iter)
    next(_iter)
    assert next(_iter) == 0

    _ = MySpecialQueue(range(1, 6))
    _.appendmiddle(0)
    _iter = iter(_)
    next(_iter)
    next(_iter)
    assert next(_iter) == 0


def test_popmiddle():
    _ = MySpecialQueue(range(1, 6))
    assert _.popmiddle() == 3

    _ = MySpecialQueue(range(1, 7))
    assert _.popmiddle() == 3

    _ = MySpecialQueue(range(1, 5))
    assert _.popmiddle() == 2
