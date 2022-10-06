"""Generic LinkedList Implementation"""
from typing import Any, Optional


class EmptyLinkedList(Exception):
    pass


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

    def append(self, data: Any):
        """Append a node to the end of LinkedList

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
        """Append a node to the start of the LinkedList

        This node will be the `head`
        """

        # Check if we have a head or not
        # if no head is available -> head is Node and tail is None too
        # then, we have to just append the data to out LinkedList :)
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
            raise EmptyLinkedList("LinkedList is empty")

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

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"{self.__class__.__name__}(head={self.head})"
