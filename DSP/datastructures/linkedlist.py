"""Generic LinkedList Implementation"""
from typing import Any, Optional


class Node:
    def __init__(self, data, next_item: Optional["Node"] = None):
        self.data = data
        self.next_item = next_item

    def __eq__(self, other):
        return self.data == other.data and self.next_item == other.next_item

    def __hash__(self):
        return hash((self.data, self.next_item))

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(data={self.data}, next_item={self.next_item})"
        )


class LinkedList:
    def __init__(self, head: Optional[Any] = None):
        if not isinstance(head, Node) and head is not None:
            self.head = Node(head)
            self._size = 1
        elif isinstance(head, Node):
            self.head = head
            self._size = 1
        else:
            self.head = head
            self._size = 0

        self.tail: Optional["Node"] = self.head

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"{self.__class__.__name__}(head={self.head})"
