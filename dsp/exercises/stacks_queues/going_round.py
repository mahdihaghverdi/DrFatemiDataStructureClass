from collections import deque
from typing import Any, Iterable, Optional


class MyDeque:
    def __init__(self, maxlen: int, /, iterable: Optional[Iterable] = None):
        self.maxlen: int = maxlen
        paras: dict[str, Any] = {"maxlen": maxlen}
        if iterable is not None:
            paras["iterable"] = iterable
        self._deque: "deque" = deque(**paras)

    def __repr__(self):
        return "MyDeque" + self._deque.__repr__()[5:]

    def __str__(self):
        return "MyDeque" + str(self._deque)[5:]


if __name__ == "__main__":
    size = int(input())
    command_count = int(input())
    for _ in range(command_count):
        command, *arg = input().split()
