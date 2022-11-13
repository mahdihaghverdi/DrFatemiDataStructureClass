from random import randint

from dsp import blc_do


def test():
    bins = [bin(randint(1, 1_000_000)) for _ in range(10_000)]
    for num in bins:
        to_pass = " ".join(num[2:])
        assert int(num[2:], 2) == blc_do(to_pass)
