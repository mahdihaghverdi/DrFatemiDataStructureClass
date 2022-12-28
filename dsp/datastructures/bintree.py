from typing import Optional


class BinTree:
    def __init__(self, root=None):
        self.root = root
        self._children: dict[str, Optional["BinTree"]] = {
            "left": None,
            "right": None,
        }

    @property
    def children(self):
        return self._children

    @property
    def left(self):
        return self._children["left"]

    @property
    def right(self):
        return self._children["right"]

    def addleft(self, node: "BinTree"):
        if self._children["left"] is not None:
            raise ValueError(f"{self.root} already has a left child")
        self._children["left"] = node

    def addright(self, node: "BinTree"):
        if self._children["right"] is not None:
            raise ValueError(f"{self.root} already has a right child")
        self._children["right"] = node

    def height(self) -> int:
        if self.root is None:
            return 0
        try:
            left = self.left.height()
        except AttributeError:
            left = 0
        try:
            right = self.right.height()
        except AttributeError:
            right = 0

        return max((left, right)) + 1
