from typing import Any, Iterator


class EmptyLinkedList(Exception):
    """Is raised when the operation is not allowed on an empty linked list"""

    def __str__(self):
        return "SinglyLinkedList is empty"


class LinkedList:
    def __iter__(self) -> Iterator[Any]:
        if self.head is None:  # type: ignore
            raise EmptyLinkedList()

        data, next_item = self.head.data, self.head.next_item  # type: ignore
        yield data
        while next_item is not None:
            data, next_item = next_item.data, next_item.next_item
            yield data
