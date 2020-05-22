import epi2.dynamic_programming_16_7 as dp


def test_scenario1():
    name = 'tedistiredman'
    sequence = ['red', 'man']
    assert 'redman' == dp.find_it(name, sequence)


def test_scenario2():
    name = 'amanaplanacanal'
    sequence = ['a', 'man', 'a', 'plan', 'a', 'canal']
    assert 'amanaplanacanal' == dp.find_it(name, sequence)


def test_scenario3():
    name = 'poobeariseating'
    sequence = ['poo', 'bear', 'care']
    assert '' == dp.find_it(name, sequence)
