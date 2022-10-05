from DSP import Node


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
