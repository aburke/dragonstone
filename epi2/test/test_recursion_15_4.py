import epi2.recursion_15_4 as rec

def test_scenario1():
    p_set = rec.power_set({1, 2, 3})
    assert p_set == [{1}, {1, 2}, {1, 2, 3}, {1, 3}, {2}, {2, 3}, {3}, set()]