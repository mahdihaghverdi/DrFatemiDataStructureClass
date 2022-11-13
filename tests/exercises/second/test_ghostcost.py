from dsp import max_sum, subseqs


def test_subseqs():
    expected = [[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
    assert subseqs([1, 2, 3]) == expected


def test_max_sum():
    assert max_sum(list(range(10))) == sum(range(10))
