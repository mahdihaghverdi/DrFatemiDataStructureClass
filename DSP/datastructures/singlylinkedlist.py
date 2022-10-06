"""Generic SinglyLinkedList Implementation"""
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


class SinglyLinkedList:
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
    """

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

    def append(self, data: Any):
        """Append a node to the end of SinglyLinkedList

        If `data` is not a node: wrap it in a node.
        """
        # Check if we have a head or not
        # if no head is available -> head is None and tail is None too
        if self.head is None:
            if not isinstance(data, Node):
                _ = Node(data)
                self.head = _
                self.tail = self.head
            else:
                self.head = data
                self.tail = self.head
        else:
            if not isinstance(data, Node):
                _ = Node(data)
                self.tail.next_item = _
                self.tail = _
                assert self.tail.next_item is None
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

        former_head = self.head
        if not isinstance(data, Node):
            _ = Node(data)
            self.head = _
            self.head.next_item = former_head
        else:
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
        to_return = None

        if isinstance(item, int):
            if item == 0:
                return self.head.data

            for _ in range(item + 1):
                try:
                    to_return = next(self_iter)
                except StopIteration:
                    raise IndexError("Index out of range") from None
            else:
                return to_return

        # item is a slice by now
        return [self[index] for index in range(item.start, item.stop, item.step)]

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"{self.__class__.__name__}(head={self.head})"