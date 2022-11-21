from collections import deque

from dsp import MyDeque


def test__init__():
    _ = MyDeque(10)
    assert _.maxlen == 10
    assert _._deque == deque(maxlen=10)
