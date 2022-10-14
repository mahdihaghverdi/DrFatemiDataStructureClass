from array import array
from itertools import zip_longest
from operator import add, sub

ops = {
    "+": add,
    "-": sub,
}


def get(num: str) -> "array[int]":
    return array("i", map(int, num.strip()))


def do(first: "array[int]", last: "array[int]", op: str) -> int:
    minus = False
    if op == "-" and (
        int("".join(str(i) for i in last)) > int("".join(str(i) for i in first))
    ):
        first, last = last, first
        minus = True

    result = array(
        "i",
        [
            ops[op](f, s)
            for f, s in zip_longest(reversed(first), reversed(last), fillvalue=0)
        ],
    )

    # 99 + 1: [10, 9]    -> [10 % 10, (10 // 10) + 9] = [0, 10]
    #                    -> [0, 10 % 10, (10 // 10) + 0] = [0, 0, 10] -> 100

    # 86 + 8: [14, 8]    -> [14 % 10, (14 // 10) + 8]: [4, 9] -> 94

    # 86 + 28: [14, 10]  -> [14 % 10, (14 // 10) + 10] = [4, 11]
    #                    -> [4, 11 % 10, (11 // 10) + 0] = [4, 1, 1] -> 114

    for idx, num in enumerate(result):
        result[idx] = num % 10
        try:
            result[idx + 1] = (num // 10) + result[idx + 1]
        except IndexError:
            if op == "+":
                result.append(0 + num // 10)
                break

    res = int("".join(str(i) for i in reversed(result)))
    return res if not minus else res * -1


if __name__ == "__main__":
    fst, op_, lst = get(input()), input(), get(input())
    print(do(fst, lst, op_))
