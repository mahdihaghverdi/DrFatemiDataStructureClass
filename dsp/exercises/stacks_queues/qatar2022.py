import math
from collections import deque
from collections.abc import Collection
from typing import Any, Generic, Iterable, Iterator, Optional, TypeVar, Union, cast

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

    def pop(self) -> Union["T", None]:
        try:
            return self._deque.pop()
        except IndexError:
            return None

    def popleft(self) -> "T":
        try:
            return self._deque.popleft()
        except IndexError:
            return None

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

    def popmiddle(self) -> Union["T", None]:
        if len(self) % 2 == 1:
            pos = math.ceil(len(self) / 2)
        else:
            pos = len(self) // 2

        lasts = []
        for _ in range(len(self) - pos):
            lasts.append(self._deque.pop())
        try:
            got = self._deque.pop()
        except IndexError:
            return None
        for item in lasts[::-1]:
            self.append(item)
        return got

    def output(self) -> str:
        return (
            (" ".join(cast(str, num) for num in self) if len(self) else "-1")
            if self
            else "-1"
        )

    def __len__(self) -> int:
        return len(self._deque)

    def __iter__(self) -> Iterator[T]:
        return iter(self._deque)

    def __contains__(self, x: object) -> bool:
        return x in self._deque

    def __repr__(self):
        return "MySpecialQueue" + self._deque.__repr__()[5:]


push_palette = {
    "PushFront": MySpecialQueue.appendleft,  # self, value
    "PushMiddle": MySpecialQueue.appendmiddle,  # self, value
    "PushBack": MySpecialQueue.append,  # self, value
}

pop_palette = {
    "PopFront": MySpecialQueue.popleft,  # self
    "PopMiddle": MySpecialQueue.popmiddle,  # self
    "PopBack": MySpecialQueue.pop,  # self
}


def do(how_much: int):
    msq: MySpecialQueue[str] = MySpecialQueue()
    for _ in range(how_much):
        command, *arg = input().split()
        if command in push_palette:
            push_palette[command](msq, arg[-1])
        else:
            pop_palette[command](msq)
    return msq.output()


if __name__ == "__main__":
    count = int(input())
    print(do(count))
