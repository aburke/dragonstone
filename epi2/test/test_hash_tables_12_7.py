import epi2.hash_table_12_7 as hsh

def test_scenario1():
    expected = hsh.SSRange(16, 14)
    paragraph = ['a', 'm', 'a', 'm', 'a', 'b', 'm', 'a', 'm', 'b', 'c', 'm', 'm', 'm', 'a', 'b', 'c']
    assert expected == hsh.search({'a', 'b', 'c'}, paragraph)

def test_scenario2():
    paragraph = ['q', 'q', 'q', 'm']
    assert hsh.SSRange(0, 0) == hsh.search({'q'}, paragraph)

def test_scenario3():
    paragraph = ['a', 'r', 'r', 'b', 'r', 'r', 'r', 'a', 'm', 'b', 'b']
    assert hsh.SSRange(9, 7) == hsh.search({'a', 'b'}, paragraph)

def test_scenario4():
    paragraph = ['a', 'b', 'c']
    assert hsh.search({'a', 'q'}, paragraph) is None