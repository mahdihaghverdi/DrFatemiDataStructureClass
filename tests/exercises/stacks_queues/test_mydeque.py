from collections import deque

from dsp import MyDeque


def test__init__():
    _ = MyDeque(10)
    assert _.maxlen == 10
    assert _._deque == deque(maxlen=10)


def test_front_rear_minus_1():
    _ = MyDeque(10)
    assert _.front() == -1
    assert _.rear() == -1


def test_front():
    _ = MyDeque(10, iterable=[1])
    assert _.front() == 1

    _ = MyDeque(10, iterable=range(5))
    assert _.front() == 4


def test_rear():
    _ = MyDeque(10, iterable=[1])
    assert _.rear() == 1

    _ = MyDeque(10, iterable=range(5))
    assert _.rear() == 0


def test_enqueue():
    _ = MyDeque(3)
    assert _.enqueue(1) is True
    assert _.front() == 1


def test_enqueue_full():
    _ = MyDeque(1)
    assert _.enqueue(1) is True
    assert _.front() == 1
    assert _.enqueue(2) is False
    assert _.front() == 1
