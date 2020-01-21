from epi2.sorting_13_10 import list_sort, Node, show_all

def test_scenario1():
    node = Node(
        4, Node(
            3, Node(
                2, Node(
                    1, Node(
                        0, None
                    )
                )
            )
        )
    )
    expected = '0 => 1 => 2 => 3 => 4 => '
    actual = show_all(list_sort(node))
    assert actual == expected


def test_scenario2():
    node = Node(
        4, Node(
            3, Node(
                9, Node(
                    3, Node(
                        5, None
                    )
                )
            )
        )
    )
    expected = '3 => 3 => 4 => 5 => 9 => '
    actual = show_all(list_sort(node))
    assert actual == expected