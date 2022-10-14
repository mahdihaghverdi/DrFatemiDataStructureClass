import sys
from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Iterable, Iterator, Optional


class LinkedListError(Exception):
    pass


class EmptyLinkedList(LinkedListError):
    """Is raised when the operation is not allowed on an empty linked list"""

    def __str__(self):
        return "SinglyLinkedList is empty"


class LinkedList(ABC):
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

    def iternodes(self):
        if self.head is None:
            raise EmptyLinkedList()

        node, next_node = self.head, self.head.next_item
        yield node
        while next_node is not None:
            node, next_node = next_node, next_node.next_item
            yield node

    @abstractmethod
    def pop(self, index: Optional[int] = None):
        pass

    @abstractmethod
    def popleft(self):
        pass

    def remove(self, index: Optional[int] = None):
        self.pop(index)

    def removeleft(self):
        self.popleft()


# Singly LinkedList implementation
@dataclass
class Node:
    """Simple node representation

    each node is like:
        --------------------
        | data | next_item |
        --------------------
    in which the data is the actual data the node is containing and next_item
    is a reference the next node.
    """

    data: Any
    next_item: Optional["Node"] = None

    def __hash__(self):
        return hash((self.data, self.next_item))


class SinglyLinkedList(LinkedList, Sequence):
    """Singly Linked List implementation

    Attributes:
        head: is the head node of the linked list, defaults to None.
        tail: is the tail node of the linked list, default to `head`.
        _size: holds the size of linked list, size is the number of nodes which are connected to each other.

    Methods:
        append: adds a node to the end of the linked list, the newest node becomes the `tail`.
        appendleft: add a node to the head of the linked list, the newses node becomes the `head`.
        pop: deletes and return the tail, or a desired index
        popleft: deletes and returns the head of the linked list.
        remove: just like pop but does not return.
        removeleft: deletes the head of the linked list.
        insert: insert a data to a specific index
        extend: just like list.extend

    Behaviours:
         '__eq__', '__ne__'
         '__hash__',       hash(obj)
         '__iter__',       iter(obj) (for i in obj)
         '__getitem__',    obj[0], obj[:10]
         '__contains__',   ob in obj, ob not in obj
         '__init__',       SLL(...)
         '__len__',        len(obj)
         '__repr__',       print, repr
         '__reversed__',   reversed(obj)
         'count',          obj.count(ob)
         'index',          obj.index(ob)
    """

    def __init__(self, head: Optional[Any] = None):
        super().__init__(head)
        self.pointer = 0

    def peek(self):
        try:
            return self[self.pointer]
        except (EmptyLinkedList, IndexError):
            return "Error!"

    def __next__(self):
        try:
            got = self[self.pointer]
        except (EmptyLinkedList, IndexError):
            return "Error!"
        else:
            self.pointer += 1
            return got

    def __getitem__(self, item: int | slice) -> Any:
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

    def pop(self, index: Optional[int] = None):
        """Pop the tail, or a desired index of sll"""
        if len(self) == 0:
            raise EmptyLinkedList()

        if index is None:
            if len(self) == 1:
                return self.popleft()

            for node in self.iternodes():
                if node.next_item == self.tail:
                    # this is the node before the tail:
                    to_ret = self.tail
                    self.tail = node
                    self.tail.next_item = None
                    self._size -= 1
                    return to_ret.data

        if isinstance(index, int):
            if index == 0:
                return self.popleft()

            to_ret = self[index]  # may raise error :)

            before_and_self_nodes = []

            for idx, node in enumerate(self.iternodes()):
                if idx == index - 1:
                    before_and_self_nodes.append(node)
                elif idx == index:
                    before_and_self_nodes.append(node)

            before_node, self_node = before_and_self_nodes
            after_node = self_node.next_item
            before_node.next_item = after_node
            self._size -= 1
            return to_ret

    def popleft(self):
        """Pop the head"""
        if self.head is None:
            raise EmptyLinkedList()

        former_head = self.head
        newer_head = self.head.next_item
        self.head = newer_head
        self._size -= 1
        return former_head.data

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

        # append it
        if index == len(self) - 1:
            self.append(data)
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

    def extend(self, data: Iterable):
        for item in data:
            self.append(_ensure_node(item))

    def __repr__(self):
        return f"{self.__class__.__name__}(head={self.head})"


def _ensure_node(data: Any) -> "Node":
    if isinstance(data, Node):
        return data
    return Node(data)


if __name__ == "__main__":
    objs = {}

    prev_obj = None
    for line in sys.stdin:
        if "KianList" in line or "peek" in line or "next" in line or "hasNext" in line:
            op, obj = line.split()

            if op == "KianList":
                prev_obj = obj
                objs[obj] = SinglyLinkedList()
                continue

            if op == "peek":
                got = objs.get(obj)
                if got is None:
                    continue
                print(got.peek())

            if op == "next":
                got = objs.get(obj)
                if got is None:
                    continue
                print(next(got))

            if op == "hasNext":
                got = objs.get(obj)
                if got is None:
                    continue
                print(True if got.pointer < len(got) else False)
        else:
            got = objs.get(prev_obj)
            if got is None:
                continue
            got.extend(line.split())
