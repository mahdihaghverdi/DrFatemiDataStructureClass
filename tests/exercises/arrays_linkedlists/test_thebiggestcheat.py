from random import randint

from dsp import do, get


def test_add_no_overflow():
    firsts = ["1", "2", "10", "13", "24", "98", "76", "54", "1001", "80402"]
    lasts = ["4", "7", "3", "1", "3", "1", "2", "4", "8", "4"]

    for f, s in zip(firsts, lasts):
        assert (int(f) + int(s)) == do(get(f), get(s), "+")


def test_add():
    nums = [str(randint(1, 500)) for _ in range(500)]

    for f, s in zip(nums, nums):
        assert (int(f) + int(s)) == do(get(f), get(s), "+")


def test_no_underflow_no_minus():
    firsts = [str(randint(25, 29)) for _ in range(50)] + [
        str(randint(53, 59)) for _ in range(50)
    ]
    lasts = [f"{randint(1, 2)}{randint(0, 4)}" for _ in range(50)] + [
        f"{randint(1, 5)}{randint(0, 3)}" for _ in range(50)
    ]

    for f, s in zip(firsts, lasts):
        assert (int(f) - int(s)) == do(get(f), get(s), "-")


def test_sub():
    nums = [str(randint(1, 500)) for _ in range(500)]

    for f, s in zip(nums, nums):
        assert (int(f) - int(s)) == do(get(f), get(s), "-")

    firsts = [str(randint(100, 150)) for _ in range(100)]
    lasts = [f"{randint(1, 9)}{randint(6, 9)}{randint(1, 9)}" for _ in range(100)]

    for f, s in zip(firsts, lasts):
        assert (int(f) - int(s)) == do(get(f), get(s), "-")
