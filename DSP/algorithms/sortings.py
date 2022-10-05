from typing import TypeVar

IntStr = TypeVar("IntStr", int, str)


def insertion_sort(iterable: list[IntStr]) -> list[IntStr]:
    for num in iterable[1:]:
        j = iterable.index(num) - 1

        while j >= 0 and iterable[j] > num:
            iterable[j + 1] = iterable[j]
            j -= 1

        iterable[j + 1] = num
    return iterable


print(insertion_sort(["z", "h", "a", "c"]))
