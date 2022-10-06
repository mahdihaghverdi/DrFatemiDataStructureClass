import string

import pytest

from DSP import EmptyLinkedList, LinkedList, Node


class TestNode:
    def test_attrs(self):
        _ = Node("Mahdi")
        assert _.data == "Mahdi"
        assert _.next_item is None

        _ = Node("Mahdi", next_item=Node(1))
        assert _.data == "Mahdi"
        assert _.next_item.data == 1  # noqa
        assert _.next_item.next_item is None  # noqa

    def test__eq__(self):
        _ = Node("Mahdi")
        assert _ == _

        __ = Node(1)
        assert _ != __

    def test__hash__(self):
        assert hash((1, None)) == hash(Node(1))
        assert hash((1, Node(1))) == hash(Node(1, Node(1)))


class TestLinkedList:
    def test_basic_attrs(self):
        _ = LinkedList()
        assert _.head is None
        assert _.tail is None

        _ = LinkedList(1)
        assert isinstance(_.head, Node)
        assert _.head.data == 1
        assert _.head.next_item is None
        assert _.head == _.tail

    def test_attrs(self):
        _ = LinkedList(1)
        _.append(2)

        assert _.head == Node(1, Node(2))
        assert _.tail == Node(2)

        _.append("Mahdi")
        assert _.head == Node(1, Node(2, Node("Mahdi")))
        assert _.tail == Node("Mahdi")

    def test__len__(self):
        _ = LinkedList()
        assert len(_) == 0

        _ = LinkedList(1)
        assert len(_) == 1

        _ = LinkedList(Node("Mahdi"))
        assert len(_) == 1

    def test__bool__(self):
        _ = LinkedList()
        assert not _
        assert not bool(_)

        _ = LinkedList(1)
        assert _

    def test_append_empty(self):
        _ = LinkedList()
        _.append(1)
        assert _.head == Node(1)
        assert _.head == _.tail
        assert len(_) == 1
        assert bool(_) is True

    def test_append_not_empty(self):
        _ = LinkedList(1)
        _.append(2)
        assert _.head == Node(1, Node(2))
        assert _.tail == Node(2)
        assert len(_) == 2
        assert bool(_) is True

    def test_appendleft_empty(self):
        _ = LinkedList()
        _.appendleft(1)
        assert _.head == Node(1)
        assert _.head == _.tail
        assert len(_) == 1
        assert bool(_) is True

    def test_appendleft_non_empty_linkedlist(self):
        _ = LinkedList(1)
        _.appendleft(2)
        assert _.head == Node(2, Node(1))
        assert _.tail == Node(1)
        assert len(_) == 2
        assert bool(_) is True

    def test_popleft_empty(self):
        _ = LinkedList()
        with pytest.raises(EmptyLinkedList):
            _.popleft()

    def test_popleft_non_empty(self):
        _ = LinkedList()
        _.append(1)
        assert _.popleft() == Node(1)
        assert len(_) == 0

        _ = LinkedList()
        _.append(1)
        _.append(2)
        assert _.popleft() == Node(1, Node(2))
        assert len(_) == 1

    def test_removeleft_empty(self):
        _ = LinkedList()
        with pytest.raises(EmptyLinkedList):
            _.removeleft()

    def test_removeleft_non_empty(self):
        _ = LinkedList()
        _.append(1)
        _.removeleft()
        assert len(_) == 0

        _ = LinkedList()
        _.append(1)
        _.append(2)
        _.removeleft()
        assert len(_) == 1

    def test__iter__empty(self):
        with pytest.raises(EmptyLinkedList):
            _ = LinkedList()
            next(iter(_))

    def test__iter__non_empty(self):
        _ = LinkedList()
        for i in range(10):
            _.append(i)

        assert list(range(10)) == list(_)

    def test__getitem__empty(self):
        _ = LinkedList()
        with pytest.raises(EmptyLinkedList):
            _[2]

        with pytest.raises(EmptyLinkedList):
            _[2:4]

    def test__getitem__non_empty(self):
        _ = LinkedList()
        for num in range(10):
            _.append(num)

        for expected in range(10):
            assert expected == _[expected]

        _ = LinkedList()
        for char in string.ascii_lowercase:
            _.append(char)

        for index, expected in zip(
            range(len(string.ascii_lowercase)),
            string.ascii_lowercase,
        ):
            assert expected == _[index]

        assert _[0:15:4] == _[0:15:4]
        assert _[0:25:3] == _[0:25:3]
        assert _[10:20:5] == _[10:20:5]
