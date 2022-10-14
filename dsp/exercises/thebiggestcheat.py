from itertools import zip_longest
from operator import add, sub

ops = {
    "+": add,
    "-": sub,
}


def get(num: str) -> list[int]:
    return list(map(int, num.strip()))


def do(first: list[int], last: list[int], op: str) -> int:
    result = [
        ops[op](f, s)
        for f, s in zip_longest(
            reversed(first),
            reversed(last),
            fillvalue=0,
        )
    ]
    return int("".join(str(i) for i in reversed(result)))
