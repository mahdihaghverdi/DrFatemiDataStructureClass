from DSP import DNode, DoublyLinkedList


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

        _ = DoublyLinkedList(1)
        assert _.head == DNode(1)
        assert _.tail == _.head
