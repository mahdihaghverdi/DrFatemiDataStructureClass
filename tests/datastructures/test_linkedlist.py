import string

import pytest

from DSP import EmptyLinkedList, Node, SinglyLinkedList


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
        _ = SinglyLinkedList()
        assert _.head is None
        assert _.tail is None

        _ = SinglyLinkedList(1)
        assert isinstance(_.head, Node)
        assert _.head.data == 1
        assert _.head.next_item is None
        assert _.head == _.tail

    def test_attrs(self):
        _ = SinglyLinkedList(1)
        _.append(2)

        assert _.head == Node(1, Node(2))
        assert _.tail == Node(2)

        _.append("Mahdi")
        assert _.head == Node(1, Node(2, Node("Mahdi")))
        assert _.tail == Node("Mahdi")

    def test__len__(self):
        _ = SinglyLinkedList()
        assert len(_) == 0

        _ = SinglyLinkedList(1)
        assert len(_) == 1

        _ = SinglyLinkedList(Node("Mahdi"))
        assert len(_) == 1

    def test__bool__(self):
        _ = SinglyLinkedList()
        assert not _
        assert not bool(_)

        _ = SinglyLinkedList(1)
        assert _

    def test_append_empty(self):
        _ = SinglyLinkedList()
        _.append(1)
        assert _.head == Node(1)
        assert _.head == _.tail
        assert len(_) == 1
        assert bool(_) is True

    def test_append_not_empty(self):
        _ = SinglyLinkedList(1)
        _.append(2)
        assert _.head == Node(1, Node(2))
        assert _.tail == Node(2)
        assert len(_) == 2
        assert bool(_) is True

    def test_appendleft_empty(self):
        _ = SinglyLinkedList()
        _.appendleft(1)
        assert _.head == Node(1)
        assert _.head == _.tail
        assert len(_) == 1
        assert bool(_) is True

    def test_appendleft_non_empty_linkedlist(self):
        _ = SinglyLinkedList(1)
        _.appendleft(2)
        assert _.head == Node(2, Node(1))
        assert _.tail == Node(1)
        assert len(_) == 2
        assert bool(_) is True

    def test_popleft_empty(self):
        _ = SinglyLinkedList()
        with pytest.raises(EmptyLinkedList):
            _.popleft()

    def test_popleft_non_empty(self):
        _ = SinglyLinkedList()
        _.append(1)
        assert _.popleft() == Node(1)
        assert len(_) == 0

        _ = SinglyLinkedList()
        _.append(1)
        _.append(2)
        assert _.popleft() == Node(1, Node(2))
        assert len(_) == 1

    def test_removeleft_empty(self):
        _ = SinglyLinkedList()
        with pytest.raises(EmptyLinkedList):
            _.removeleft()

    def test_removeleft_non_empty(self):
        _ = SinglyLinkedList()
        _.append(1)
        _.removeleft()
        assert len(_) == 0

        _ = SinglyLinkedList()
        _.append(1)
        _.append(2)
        _.removeleft()
        assert len(_) == 1

    def test__iter__empty(self):
        with pytest.raises(EmptyLinkedList):
            _ = SinglyLinkedList()
            next(iter(_))

    def test__iter__non_empty(self):
        _ = SinglyLinkedList()
        for i in range(10):
            _.append(i)

        assert list(range(10)) == list(_)

    def test__getitem__empty(self):
        _ = SinglyLinkedList()
        with pytest.raises(EmptyLinkedList):
            _[2]

        with pytest.raises(EmptyLinkedList):
            _[2:4]

    def test__getitem__non_empty(self):
        _ = SinglyLinkedList()
        for num in range(10):
            _.append(num)

        for expected in range(10):
            assert expected == _[expected]

        _ = SinglyLinkedList()
        for char in string.ascii_lowercase:
            _.append(char)

        for index, expected in zip(
            range(len(string.ascii_lowercase)),
            string.ascii_lowercase,
        ):
            assert expected == _[index]

        assert _[0:15:4] == list(string.ascii_lowercase[0:15:4])
        assert _[0:25:3] == list(string.ascii_lowercase[0:25:3])
        assert _[10:20:5] == list(string.ascii_lowercase[10:20:5])
        assert _[-10] == string.ascii_lowercase[-10]
        assert _[-10:2:-2] == list(string.ascii_lowercase[-10:2:-2])
