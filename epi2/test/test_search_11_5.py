import epi2.search_11_5 as search

def test_scenario1():
    expected = 5
    actual = search.compute_square_root(25)
    assert actual == expected

def test_scenario2():
    expected = 6.3245
    actual = search.compute_square_root(40)
    assert actual == expected