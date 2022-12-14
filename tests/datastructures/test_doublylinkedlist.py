import pathlib
import sys

import pytest

sys.path += [str(pathlib.Path(__file__).parent.parent.parent)]

from dsp import DNode, DoublyLinkedList, EmptyLinkedList  # noqa


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

        _ = DoublyLinkedList()
        for num in range(10):
            _.append(num)

        assert len(_) == 10

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

    def test_pop_empty(self):
        with pytest.raises(EmptyLinkedList):
            _ = DoublyLinkedList()
            _.pop()

    def test_pop_one_item(self):
        _ = DoublyLinkedList(0)
        got = _.pop()
        assert 0 == got
        assert len(_) == 0

    def test_pop(self):
        _ = DoublyLinkedList(0)
        _.append(1)
        assert _.pop() == 1
        assert len(_) == 1

        _ = DoublyLinkedList()
        for num in range(10):
            _.append(num)

        _.pop()
        _.pop()
        last = _.pop()
        assert len(_) == 7
        assert last == 7

    def test_popleft_empty(self):
        with pytest.raises(EmptyLinkedList):
            _ = DoublyLinkedList()
            _.popleft()

    def test_popleft_one_item(self):
        _ = DoublyLinkedList(0)
        assert _.popleft() == 0
        assert len(_) == 0
        assert not _

    def test_popleft(self):
        _ = DoublyLinkedList()
        for num in range(10):
            _.append(num)

        got = [_.popleft() for __ in range(5)]
        assert len(_) == 5
        assert got[-1] == 4

    def test_iternodes(self):
        _ = DoublyLinkedList()
        for num in range(10):
            _.append(num)
        nodes = list(_.iternodes())
        assert len(nodes) == 10
        assert all(isinstance(i, DNode) for i in nodes)

    def test__iter__(self):
        _ = DoublyLinkedList()
        for num in range(10):
            _.append(num)

        assert list(range(10)) == list(_)
