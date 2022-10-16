import pathlib
import string
import sys

import pytest

sys.path += [str(pathlib.Path(__file__).parent.parent.parent)]

from dsp import CircularlyLinkedList, EmptyLinkedList  # noqa


def test_basic_attrs():
    _ = CircularlyLinkedList()
    assert _.head is None
    assert _.tail is None

    _ = CircularlyLinkedList(1)
    assert _.head.data == 1
    assert _.head.next_item.next_item == _.head
    assert _.tail == _.head
    assert _.tail.next_item == _.head


def test_append_empty():
    _ = CircularlyLinkedList()
    _.append(1)

    assert len(_) == 1
    assert _
    assert _.head.data == 1
    assert _.head.next_item.next_item == _.head
    assert _.tail == _.head
    assert _.tail.next_item == _.head


def test_append_non_empty():
    _ = CircularlyLinkedList(0)
    _.append(1)
    _.append(2)
    assert _.head.data == 0
    assert _.tail.data == 2
    assert _.head.next_item.data == 1
    assert _.tail.next_item.data == 0
    assert _.tail.next_item == _.head
    assert len(_) == 3


def test_appendleft_empty():
    _ = CircularlyLinkedList()
    _.appendleft(1)
    assert _.head.data == 1
    assert _.head == _.tail
    assert len(_) == 1
    assert bool(_) is True


def test_appendleft_non_empty_linkedlist():
    _ = CircularlyLinkedList(1)
    _.appendleft(2)
    assert _.head.data == 2
    assert _.tail.data == 1
    assert _.tail.next_item.data == 2


def test_pop_empty():
    with pytest.raises(EmptyLinkedList):
        _ = CircularlyLinkedList()
        _.pop()


def test_pop_one():
    _ = CircularlyLinkedList(1)
    assert _.pop() == 1
    assert len(_) == 0
    assert not _


# def test_pop():
#     # nothing passed to `pop`
#     _ = CircularlyLinkedList()
#     _.extend(range(10))
#
#     got = [_.pop() for __ in range(5)]
#     assert len(_) == 5
#     assert got[-1] == 5
#
#     assert _.tail.data == 4
#     assert _.tail.next_item == _.head
#
#     # `int` passed to pop (as an index)
#     _ = CircularlyLinkedList()
#     _.extend(string.ascii_lowercase)
#
#     c = _.pop(2)
#     assert c == "c"
#     assert len(_) == len(string.ascii_lowercase) - 1
#     assert [char for char in string.ascii_lowercase if char != "c"] == list(_)
#
#
# def test_popleft_empty():
#     _ = CircularlyLinkedList()
#     with pytest.raises(EmptyLinkedList):
#         _.popleft()
#
#
# def test_popleft_non_empty():
#     _ = CircularlyLinkedList()
#     _.append(1)
#     assert _.popleft() == 1
#     assert len(_) == 0
#
#     _ = CircularlyLinkedList()
#     _.append(1)
#     _.append(2)
#     assert _.popleft() == 1
#     assert len(_) == 1
