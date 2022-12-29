import ast
from typing import Dict, Optional


class BinTree:
    def __init__(self, root=None):
        self.root = root
        self._children: Dict[str, Optional["BinTree"]] = {
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

        if node != "null":
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

    @classmethod
    def fromlist(cls, data: list, root: int = 0):
        if not data:
            raise ValueError("Empty list")

        tree = None
        if root < len(data):
            if data[root] is not None:
                tree = BinTree(data[root])
                tree.addleft(cls.fromlist(data, 2 * root + 1))
                tree.addright(cls.fromlist(data, 2 * root + 2))
        return tree

    def isbalanced(self):
        if self.left is None and self.right is None:
            return True
        if (left := self.left) is not None and self.right is None:
            return (abs(left.height() - 0) <= 1) and left.isbalanced()
        if self.left is None and (right := self.right) is not None:
            return (abs(right.height() - 0) <= 1) and right.isbalanced()
        return (abs(self.left.height() - self.right.height()) <= 1) and (
            self.left.isbalanced() and self.right.isbalanced()
        )

    def __repr__(self):
        return f"BinTree(root={self.root}, children={self.children})"


if __name__ == "__main__":
    parsed_input = input().replace("null", "None")
    input_list = ast.literal_eval(parsed_input)
    if not input_list:
        print(True)
        exit()
    print(BinTree.fromlist(input_list))
