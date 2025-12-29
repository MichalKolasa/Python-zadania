import pytest
from zadanie_11_2 import Node, SingleList

""" Testy metod dopisanych do klasy SingleList: search(), find_max(), find_min() oraz reverse() """

@pytest.mark.parametrize(
    "values, search_value, found",
    [
        ([1, 2, 3], 2, True),
        ([1, 2, 3], 4, False),
        ([5], 5, True),
        ([], 1, False),
    ]
)
def test_search(values, search_value, found):
    list = SingleList()
    for v in values:
        list.insert_tail(Node(v))

    node = list.search(search_value)

    if found:
        assert node is not None
        assert node.data == search_value
    else:
        assert node is None


@pytest.mark.parametrize(
    "values, expected_min, expected_max",
    [
        ([1, 2, 3], 1, 3),
        ([3, 2, 1], 1, 3),
        ([5, 5, 5], 5, 5),
        ([-1, 10, 0], -1, 10),
    ]
)
def test_find_min_max(values, expected_min, expected_max):
    list = SingleList()
    for v in values:
        list.insert_tail(Node(v))

    assert list.find_min().data == expected_min
    assert list.find_max().data == expected_max


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, -2, 3, -4], [-4, 3, -2, 1])
    ]
)
def test_reverse(values, expected):
    list = SingleList()
    for v in values:
        list.insert_tail(Node(v))

    list.reverse()

    result = []
    current = list.head
    while current:
        result.append(current.data)
        current = current.next

    assert result == expected
    assert list.count() == len(values)

    if values:
        assert list.head.data == expected[0]
        assert list.tail.data == expected[-1]
