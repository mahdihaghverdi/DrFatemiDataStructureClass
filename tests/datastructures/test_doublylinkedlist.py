import pathlib
import sys

sys.path += [str(pathlib.Path(__file__).parent.parent.parent)]

from DSP import DNode, DoublyLinkedList  # noqa


class TestDNode:
    def test_attrs(self):
        _ = DNode(2)
        assert _.data == 2
        assert _.prev_item is None
        assert _.next_item is None

    def test__eq__(self):
        _ = DNode(1)
        assert _ == DNode(1)
        assert _ != DNode(None)

    def test__hash__(self):
        assert hash(DNode(1)) == hash((1, None, None))


class TestDoublyLinkedList:
    def test_attrs(self):
        _ = DoublyLinkedList()
        assert _.head is None
        assert _.tail is None
        assert len(_) == 0

        _ = DoublyLinkedList(1)
        assert _.head == DNode(1)
        assert _.tail == _.head
        assert len(_) == 1

    def test__len__(self):
        _ = DoublyLinkedList()
        assert len(_) == 0

        _ = DoublyLinkedList(1)
        assert len(_) == 1

    def test__bool__(self):
        _ = DoublyLinkedList()
        assert not _
        assert bool(_) is False

        _ = DoublyLinkedList(1)
        assert _
        assert bool(_) is True

    def test_append_empty(self):
        _ = DoublyLinkedList()
        _.append(1)

        assert len(_) == 1
        assert _.head.data == 1
        assert _.head.next_item is None
        assert _.tail == _.head

    def test_append(self):
        _ = DoublyLinkedList(1)
        _.append(2)

        assert len(_) == 2
        assert _.head.next_item.data == 2
        assert _.head.next_item.next_item is None
        assert _.head.next_item == _.tail
        assert _.tail.prev_item == _.head

        _.append(3)
        assert len(_) == 3
        assert _.tail.data == 3
        assert _.tail.next_item is None
        assert _.tail.prev_item.data == 2
        assert _.tail.prev_item.next_item == _.tail

    def test_appendleft_empty(self):
        _ = DoublyLinkedList()
        _.appendleft(1)

        assert len(_) == 1
        assert _.head.data == 1
        assert _.head.next_item is None
        assert _.tail == _.head

    def test_appendleft(self):
        _ = DoublyLinkedList(1)
        _.appendleft(0)

        assert len(_) == 2
        assert _.head.data == 0
        assert _.head.next_item.data == 1
        assert _.head.next_item.prev_item.data == 0
        assert _.tail.data == 1
        assert _.tail.next_item is None
        assert _.tail.prev_item.data == 0

        _.appendleft(-1)
        assert len(_) == 3
        assert _.head.data == -1
        assert _.head.next_item.data == 0
        assert _.head.next_item.prev_item.data == -1
        assert _.tail.data == 1
        assert _.tail.next_item is None
        assert _.tail.prev_item.data == 0
