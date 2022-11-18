from itertools import combinations
from sys import stdin
from typing import List, Sequence


def subseqs(sequence: Sequence) -> List[List[int]]:
    def key(subseq):
        return len(subseq)

    to_ret = [[num] for num in sequence]
    to_ret.extend(
        [
            sequence[start: end + 1]  # type: ignore
            for start, end in (combinations(range(len(sequence)), 2))
        ],
    )
    return sorted(to_ret, key=key)


def max_sum(sequence: List[int]) -> int:
    return max(sum(subseq) for subseq in subseqs(sequence))


def do():
    _ = int(input())
    all_ghosts: List[List[int]] = []

    for idx, line in enumerate(stdin):
        if (-1) ** idx == 1:
            continue
        all_ghosts.append(list(map(int, line.split())))

    for ghost_group in all_ghosts:
        print(max_sum(ghost_group))


if __name__ == "__main__":
    do()
