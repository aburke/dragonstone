import epi2.heaps_10_5 as heap

def test_scenario1():
    ip = [1, 0, 3, 5, 2, 0, 1]
    expected = [1, 0.5, 1, 2, 2, 1.5, 1]
    mc = heap.MedianCalc()
    for e in ip:
        mc.calculate_median(e)

    assert expected == mc.medians

def test_scenario2():
    ip = [2, 2, 1, 2, 2]
    expected = [2, 2, 2, 2, 2]
    mc = heap.MedianCalc()
    for e in ip:
        mc.calculate_median(e)
    assert expected == mc.medians

def test_scenario3():
    ip = [1, 3, -1, -5, 2]
    expected = [1, 2, 1, 0, 1]
    mc = heap.MedianCalc()
    for e in ip:
        mc.calculate_median(e)
    assert expected == mc.medians


    