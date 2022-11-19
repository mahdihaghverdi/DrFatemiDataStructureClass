import itertools


def istriangle(a: int, b: int, c: int) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)


def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


def three_nums(n: int):
    combs = [
        comb
        for comb in combinations_with_replacement(range(1, n + 1), 3)
        if sum(comb) == n and istriangle(*comb)
    ]
    print(combs)
    return len(combs)


def do():
    sum_ = int(input())
    return three_nums(sum_)


if __name__ == '__main__':
    print(do())
