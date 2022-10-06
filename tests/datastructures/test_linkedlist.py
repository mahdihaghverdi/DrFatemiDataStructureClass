from DSP import LinkedList, Node


class TestNode:
    def test_attrs(self):
        _ = Node("Mahdi")
        assert _.data == "Mahdi"
        assert _.next_item is None

        _ = Node("Mahdi", next_item=Node(1))
        assert _.data == "Mahdi"
        assert _.next_item.data == 1
        assert _.next_item.next_item is None

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

    def test_append_empty_linkedlist(self):
        _ = LinkedList()
        _.append(1)
        assert len(_) == 1
        assert bool(_) is True

    def test_append_not_empty_linkedlist(self):
        _ = LinkedList(1)
        _.append(2)
        assert len(_) == 2
        assert bool(_) is True
