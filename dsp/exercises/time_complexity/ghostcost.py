from itertools import combinations
from sys import stdin
from typing import List, Sequence


def subseqs(sequence: Sequence):
    def key(subseq):
        return len(subseq)

    to_ret = [(num,) for num in sequence]
    to_ret.extend(
        [
            tuple(sequence[start: end + 1])  # type: ignore
            for start, end in (combinations(range(len(sequence)), 2))
        ],
    )
    return sorted(to_ret, key=key)


def max_sum(sequence: List[int]) -> int:
    return max(sum(subseq) for subseq in subseqs(sequence))


def do():
    _ = int(input())

    for idx, line in enumerate(stdin):
        if (-1) ** idx == 1:
            continue
        print(max_sum(list(map(int, line.split()))))


if __name__ == "__main__":
    do()
