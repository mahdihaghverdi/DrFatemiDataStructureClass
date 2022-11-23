import math
from collections import deque
from collections.abc import Collection
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


class MySpecialQueue(Generic[T], Collection):
    def __init__(self, iterable: Optional[Iterable] = None):
        paras = {}
        if iterable is not None:
            paras["iterable"] = iterable
        self._deque: "deque[T]" = deque(**paras)  # type: ignore

    def append(self, value: "T"):
        self._deque.append(value)

    def appendleft(self, value: "T"):
        self._deque.appendleft(value)

    def pop(self) -> "T":
        return self._deque.pop()

    def popleft(self) -> "T":
        return self._deque.popleft()

    def appendmiddle(self, value: "T"):
        pos = len(self) // 2
        lasts = []
        if len(self) % 2 == 0:
            for _ in range(pos):
                lasts.append(self._deque.pop())
        else:
            for _ in range(pos + 1):
                lasts.append(self._deque.pop())

        self._deque.append(value)
        for item in lasts[::-1]:
            self._deque.append(item)

    def popmiddle(self) -> "T":
        if len(self) % 2 == 1:
            pos = math.ceil(len(self) / 2)
        else:
            pos = len(self) // 2

        for _ in range(len(self) - pos):
            self._deque.pop()
        return self._deque.pop()

    def __len__(self) -> int:
        return len(self._deque)

    def __iter__(self) -> Iterator[T]:
        return iter(self._deque)

    def __contains__(self, x: object) -> bool:
        return x in self._deque

    def __repr__(self):
        return "MySpecialQueue" + self._deque.__repr__()[5:]
