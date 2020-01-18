import epi2.search_11_10 as search

def test_scenario1():
    expected = (5, 3)
    actual = search.find_duplicate_and_missing([0, 1, 2, 5, 5, 4])
    assert expected == actual

def test_scenario2():
    expected = (1, 0)
    actual = search.find_duplicate_and_missing([3, 1, 2, 5, 1, 4])
    assert expected == actual