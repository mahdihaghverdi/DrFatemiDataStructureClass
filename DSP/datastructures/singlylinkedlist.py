"""Generic SinglyLinkedList Implementation"""
from collections.abc import Sequence
from typing import Any, Iterator, Optional, Union


class EmptyLinkedList(Exception):
    """Is raised when the operation is not allowed on an empty linked list"""

    def __str__(self):
        return "SinglyLinkedList is empty"


class Node:
    """Simple node representation

    each node is like:
        --------------------
        | data | next_item |
        --------------------
    in which the data is the actual data the node is containing and next_item
    is a reference the next node.
    """

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


class SinglyLinkedList(Sequence):
    """Singly Linked List implementation

    Attributes:
        head: is the head node of the linked list, defaults to None.
        tail: is the tail node of the linked list, default to `head`.
        _size: holds the size of linked list, size is the number of nodes which are connected to each other.

    Methods:
        append: adds a node to the end of the linked list, the newest node becomes the `tail`.
        appendleft: add a node to the head of the linked list, the newses node becomes the `head`.
        popleft: deletes and returns the head of the linked list.
        removeleft: deletes the head of the linked list.

    Behaviours:
        len(): returns the size of the linked list.
        iter(): returns an iterator of the data of linked list
        singly_linked_list[start[, stop, step]]: works just like sequence types slices.
        Something in singly_linked_list
    """

    def __init__(self, head: Optional[Any] = None):
        if head is not None:
            self.head = _ensure_node(head)
            self._size = 1
        else:
            self.head = head
            self._size = 0
        self.tail: Optional["Node"] = self.head

    def __iter__(self) -> Iterator[Any]:
        if self.head is None:
            raise EmptyLinkedList()

        data, next_item = self.head.data, self.head.next_item
        yield data
        while next_item is not None:
            data, next_item = next_item.data, next_item.next_item
            yield data

    def __getitem__(self, item: Union[int, slice]) -> Any:
        if not self:
            raise EmptyLinkedList()

        self_iter = iter(self)
        data = None

        if isinstance(item, int):
            item = item if item >= 0 else item + self._size
            if item == 0:
                return self.head.data

            for _ in range(item + 1):
                try:
                    data = next(self_iter)
                except StopIteration:
                    raise IndexError("Index out of range") from None
            else:
                return data

        # item is a slice now
        return [
            self[index]
            for index in range(
                item.start if item.start >= 0 else self._size + item.start,
                item.stop,
                item.step,
            )
        ]

    def __len__(self):
        return self._size

    def append(self, data: Any):
        """Append a node to the end of SinglyLinkedList

        If `data` is not a node: wrap it in a node.
        """

        # Check if we have a head or not
        # if no head is available -> head is None and tail is None too
        data = _ensure_node(data)
        if self.head is None:
            self.tail = self.head = data
        else:
            self.tail.next_item = data
            self.tail = data
            assert self.tail.next_item is None
        self._size += 1

    def appendleft(self, data: Any):
        """Append a node to the start of the SinglyLinkedList

        This node will be the `head`
        """

        # Check if we have a head or not
        # if no head is available -> head is Node and tail is None too
        # then, we have to just append the data to out SinglyLinkedList :)
        if self.head is None:
            self.append(data)
            return

        data = _ensure_node(data)
        former_head = self.head
        self.head = data
        self.head.next_item = former_head
        self._size += 1

    def popleft(self):
        """Pop the head"""
        if self.head is None:
            raise EmptyLinkedList()

        former_head = self.head
        newer_head = self.head.next_item
        self.head = newer_head
        self._size -= 1
        return former_head

    def removeleft(self):
        """Remove the head and NOT return it

        This method just calls `popleft` method but does not return the value returned by popleft.
        """
        self.popleft()

    def insert(self, index: int, data: Any):
        """Insert a node at the given

        >>> a = [1]
        >>> a.insert(0, 0)
        >>> # a -> [0, 1]
        """

        if self._size == 0:
            self.append(data)
            return

        # if index == 0: it will be inserted at the head
        if index == 0:
            self.appendleft(data)
            return

        where_data = self[index]
        former_node = self.head

        while True:
            if former_node.next_item.data == where_data:
                _ = _ensure_node(data)
                later_node = former_node.next_item
                former_node.next_item = _
                _.next_item = later_node
                self._size += 1
                return
            former_node = former_node.next_item

    def __repr__(self):
        return f"{self.__class__.__name__}(head={self.head})"


def _ensure_node(data: Any) -> "Node":
    if isinstance(data, Node):
        return data
    return Node(data)
