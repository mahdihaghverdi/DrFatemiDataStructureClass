from collections import deque
from typing import Any, Generic, Iterable, Optional, TypeVar, Union

T = TypeVar("T")


#  deque -> (entrance [appendleft]) [1, 2, 3, 4, 5] (exit [pop])
class MyDeque(Generic[T]):
    def __init__(self, maxlen: int, /, iterable: Optional[Iterable] = None):
        self.maxlen: int = maxlen
        paras: dict[str, Any] = {"maxlen": maxlen}
        if iterable is not None:
            paras["iterable"] = iterable
        self._deque: "deque[T]" = deque(**paras)

    def front(self) -> Union[T, int]:
        try:
            got = self._deque.pop()
            self._deque.append(got)
            return got
        except IndexError:
            return -1

    def rear(self) -> Union[T, int]:
        try:
            got = self._deque.popleft()
            self._deque.appendleft(got)
            return got
        except IndexError:
            return -1

    def enqueue(self, value: "T"):
        if len(self._deque) < self.maxlen:
            self._deque.appendleft(value)
            return True
        return False

    def __repr__(self):
        return "MyDeque" + self._deque.__repr__()[5:]

    def __str__(self):
        return "MyDeque" + str(self._deque)[5:]


if __name__ == "__main__":
    size = int(input())
    command_count = int(input())
    for _ in range(command_count):
        command, *arg = input().split()
