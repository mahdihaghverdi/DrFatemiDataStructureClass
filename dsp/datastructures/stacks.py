from abc import ABC
from collections.abc import Collection
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


class _Stack(Generic[T], ABC):
    def __init__(self, iterable: Optional[Iterable["T"]] = None):
        if iterable is None:
            self._stack: list["T"] = []
            return
        self._stack = list(iterable)

    def __iter__(self) -> Iterator["T"]:
        """Make Stacks iterable

        To make stacks iterables, we should have sequential pops and appends
        stack = [1, 2, 3, 4, 5]
        for item in stack:
            ...

        --> pop -> yield 5
                -> yield 4
                -> yield 3
                -> yield 2
                -> yield 1
        --> append <- 1
                   <- 2
                   <- 3
                   <- 4
                   <- 5

        Time Complexity of __iter__ will be O(n)
        """
        yielded: list["T"] = []
        while True:
            try:
                got = self._stack.pop()
            except IndexError:
                break
            else:
                yielded.append(got)
                yield got
        self._stack.extend(yielded)

    def append(self, item: "T"):
        self._stack.append(item)

    def pop(self) -> "T":
        return self._stack.pop()

    def __len__(self) -> int:
        return len(self._stack)

    def __contains__(self, x: object) -> bool:
        """Implement `in` behaviour for our stacks

        Note that we `can` use the __contains__ of underlying list
        but then the complexity of the stack won't be O(n) which `has to be`
        in order to make time complexity O(n) we have to iterate through
        """
        for item in self:
            if item == x:
                return True
        return False


class Stack(_Stack["T"], Collection):
    pass


class StrStack(_Stack[str], Collection):
    pass


class IntStack(_Stack[int], Collection):
    pass
