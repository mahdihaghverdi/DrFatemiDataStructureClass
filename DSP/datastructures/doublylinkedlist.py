from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class DNode:
    data: Any
    prev_item: Optional["DNode"] = None
    next_item: Optional["DNode"] = None

    def __hash__(self):
        return hash((self.data, self.prev_item, self.next_item))
