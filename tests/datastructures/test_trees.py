import pytest

from dsp import TreeNode


class TestTreeNode:
    @classmethod
    def setup_class(cls):
        cls.data = 1
        cls.root_tree_node_no_child = TreeNode(data=cls.data)  # noqa

        cls.children = [TreeNode(data=cls.data), TreeNode(cls.data)]  # noqa
        cls.root_tree_node_with_children = TreeNode(data=cls.data, children=cls.children)  # noqa

    def test_root_no_child_attrs(self):
        assert self.root_tree_node_no_child.data == self.data
        assert self.root_tree_node_no_child.parent is None
        assert self.root_tree_node_no_child.children is None

        with pytest.raises(TypeError):
            TreeNode(self.data, parent=1)  # noqa

    def test_root_with_child_attrs(self):
        assert self.root_tree_node_with_children.children
        assert len(self.root_tree_node_with_children.children) == 2
        for child in self.root_tree_node_with_children.children:
            assert child.data == self.data
            assert child.parent == self.root_tree_node_with_children
