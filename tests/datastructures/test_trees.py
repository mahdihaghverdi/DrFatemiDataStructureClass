# import pytest
#
# from dsp import TreeNode
#
#
# class TestTreeNode:
#     @classmethod
#     def setup_class(cls):
#         cls.data = 1
#         cls.root_tree_node_no_child = TreeNode(data=cls.data)  # noqa
#
#         cls.children = [TreeNode(cls.data), TreeNode(cls.data)]  # noqa
#         cls.root_tree_node_with_children = TreeNode(
#             data=cls.data,
#             children=cls.children,
#         )  # noqa
#
#     def test_root_no_child_attrs(self):
#         assert self.root_tree_node_no_child.data == self.data
#         assert self.root_tree_node_no_child.parent is None
#         assert self.root_tree_node_no_child.children is None
#
#         with pytest.raises(TypeError):
#             TreeNode(self.data, parent=1)  # noqa
#
#     def test_root_with_child_attrs(self):
#         assert self.root_tree_node_with_children.children
#         assert len(self.root_tree_node_with_children.children) == 2
#         for child in self.root_tree_node_with_children.children:
#             assert child.data == self.data
#             assert child.parent == self.root_tree_node_with_children
#
#     def test__eq__(self):
#         assert self.root_tree_node_no_child != self.root_tree_node_with_children
#         assert TreeNode(data=self.data) == self.root_tree_node_no_child
#
#     def test__hash__(self):
#         assert hash(self.root_tree_node_no_child) == hash((self.data, None, None))
#         assert hash(self.root_tree_node_with_children) == hash(
#             (self.data, None, len(self.root_tree_node_with_children.children)),
#         )
import pytest

from dsp import BinTree


class TestBinTree:
    def test_adds(self):
        _ = BinTree(0)
        _.addleft(BinTree(1))
        assert _.left
        assert _.left.root == 1

        _.addright(BinTree(2))
        assert _.right
        assert _.right.root == 2

        with pytest.raises(ValueError):
            _.addleft(BinTree(2))

        with pytest.raises(ValueError):
            _.addright(BinTree(2))

    def test_height(self):
        _ = BinTree()
        assert _.height() == 0

        _ = BinTree(5)
        assert _.height() == 1

        _ = BinTree(1)
        _.addleft(BinTree(1))
        assert _.height() == 2

        _.addright(BinTree(2))
        assert _.height() == 2

        _.left.addright(BinTree(2))
        assert _.height() == 3

        _.left.addleft(BinTree(3))
        assert _.height() == 3
