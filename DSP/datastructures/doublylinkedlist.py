from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Iterator, Optional

from .singlylinkedlist import EmptyLinkedList


@dataclass
class DNode:
    data: Any
    prev_item: Optional["DNode"] = None
    next_item: Optional["DNode"] = None

    def __hash__(self):
        return hash((self.data, self.prev_item, self.next_item))


class DoublyLinkedList(Sequence):
    def __init__(self, head: Optional[Any] = None):
        if head is not None:
            self.head = _ensure_dnode(head)
            self._size = 1
        else:
            self.head = head
            self._size = 0
        self.tail: Optional["DNode"] = self.head

    def __getitem__(self, index: int | slice):
        pass

    def __len__(self):
        return self._size

    def append(self, data: Any):
        """Append a Dnode to DoublyLinkedList

        Ensure data is a Dnode.
        """

        data = _ensure_dnode(data)
        if self.head is None:
            self.tail = self.head = data
        else:
            self.tail.next_item = data
            data.prev_item = self.tail
            self.tail = data
            assert self.tail.next_item is None
        self._size += 1

    def __repr__(self):
        return f"{self.__class__.__name__}(head={self.head})"


def _ensure_dnode(data: Any) -> "DNode":
    if isinstance(data, DNode):
        return data
    return DNode(data)
