from dsp import CSinglyLinkedList


def test_peek():
    _ = CSinglyLinkedList()
    assert _.peek() == "Error!"

    _.append(1)
    assert _.peek() == 1
    assert _.peek() == 1
    assert _.peek() == 1
    assert _.peek() == 1


def test_next():
    _ = CSinglyLinkedList()
    assert next(_) == "Error!"

    _.append(1)
    assert next(_) == 1
    assert _.pointer == 1
    assert next(_) == "Error!"

    _ = CSinglyLinkedList()
    _.append(1)
    _.append(2)
    assert next(_) == 1
    assert next(_) == 2
    assert next(_) == "Error!"

    _ = CSinglyLinkedList()
    _.extend(range(5))

    assert next(_) == 0
    assert next(_) == 1
    assert next(_) == 2
    assert next(_) == 3
    assert next(_) == 4
    assert next(_) == "Error!"
