from typing import Any, Generic, Optional, TypeVar, Union

T = TypeVar("T")


class TreeNode(Generic[T]):
    """Base Tree Node class

    All trees have nodes which their nodes are similar in many ways:
      They have:
        - data
        - parent
        - children
    """

    def __init__(
        self,
        data: Optional["T"] = None,
        *,
        parent: Optional["TreeNode[T]"] = None,
        children: Optional[list[Union["TreeNode[T]", "T"]]] = None,
    ):
        self.data = data

        if parent is not None and not isinstance(parent, TreeNode):
            raise TypeError("Parent must be of type: `TreeNode`")
        self.parent = parent

        if children is not None:
            self.children = [
                _ensure_tree_node(child).make_child_of(self) for child in children
            ]
        else:
            self.children = children

    def make_child_of(self, parent: "TreeNode[T]"):
        """Make self a children of `parent` parameter"""
        if self == parent:
            raise ValueError("Cannot make itself a parent for itself")
        self.parent = parent
        return self


def _ensure_tree_node(data: Any) -> "TreeNode":
    if isinstance(data, TreeNode):
        return data
    return TreeNode(data)
