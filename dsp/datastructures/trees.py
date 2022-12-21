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
        if parent is not None:
            parent._make_child_of(self)

        self.children = children
        if children is not None:
            self.children = [
                _ensure_tree_node(child)._make_child_of(self) for child in children
            ]

    def _make_child_of(self, parent: "TreeNode[T]"):
        """Make self a children of `parent` parameter"""
        if self == parent:
            raise ValueError("Cannot make itself a parent for itself")
        self.parent = parent
        return self

    def __eq__(self, other):
        return (
            self.data == other.data
            and self.parent == other.parent
            and self.children == other.children
        )

    def __hash__(self):
        return hash(
            (self.data, self.parent, len(self.children) if self.children else None),
        )

    def __repr__(self):
        children = None
        if self.children is not None:
            children_classes = ", ".join(
                [
                    f"{child.__class__.__name__}(data={child.data})"
                    for child in self.children
                ],
            )
            children = f"[{children_classes}]"
        return (
            f"{self.__class__.__name__}"
            f"(data={self.data}, "
            f"parent={self.__class__.__name__}({self.parent.data}), "
            f"children={children})"
        )


def _ensure_tree_node(data: Any) -> "TreeNode":
    if isinstance(data, TreeNode):
        return data
    return TreeNode(data)
