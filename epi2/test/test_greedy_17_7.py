import epi2.greedy_17_7 as greedy


def test_scenario1():
    heights = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
    assert greedy.get_max_bucket(heights) == 48