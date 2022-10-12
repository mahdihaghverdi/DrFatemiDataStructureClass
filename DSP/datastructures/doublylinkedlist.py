from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Optional

from .generallinkedlist import LinkedList


@dataclass
class DNode:
    """Class to create a two-way node

    each d-node is like:
        --------------------------------
        | prev_item | data | next_item |
        -------------------------------

    But the API is designed to instantiate a DNode as:
    dnode = DNode(data, prev_item=None, next_item=None)
    This is much better than DNode(prev_item, data, next_item=None)
    """

    data: Any
    prev_item: Optional["DNode"] = None
    next_item: Optional["DNode"] = None

    def __hash__(self):
        return hash((self.data, self.prev_item, self.next_item))


class DoublyLinkedList(LinkedList, Sequence):
    """Doubly Linked List implementation

    Attributes:
        head: the head of dll -> prev_item is always None, Default: None.
        tail: the tail of dll -> next_item is always None, Default: `head`
        _size holds the size of the dll

    Methods:
        append: adds a dnode to the end dll, the newest dnode becomes the tail
        appendleft: adds a dnode to the head, the newest dnode becomes the head

    """

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

    def appendleft(self, data: Any):
        """Append at the head of DoublyLinkedList

        Ensure data is a Dnode
        """

        if self.head is None:
            self.append(data)
            return

        data = _ensure_dnode(data)
        former_head = self.head
        self.head = data
        self.head.next_item = former_head
        former_head.prev_item = self.head
        self._size += 1

    def __repr__(self):
        return f"{self.__class__.__name__}(head={self.head})"


def _ensure_dnode(data: Any) -> "DNode":
    if isinstance(data, DNode):
        return data
    return DNode(data)
