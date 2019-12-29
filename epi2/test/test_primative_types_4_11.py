import epi2.primative_types_4_11 as pt

def test_scenario1():
    r1 = pt.Rectangle(1, 0, 9, 7)
    r2 = pt.Rectangle(4, 2, 2, 2)
    expected_rec = pt.Rectangle(4, 2, 2, 2)
    actual_rec = pt.get_rectangle_intersect(r1, r2)
    assert expected_rec == actual_rec

def test_scenario2():
    r1 = pt.Rectangle(1, -1, 5, 4)
    r2 = pt.Rectangle(2, 0, 8, 4)
    expected_rec = pt.Rectangle(x=2, y=0, width=4, height=3)
    actual_rec = pt.get_rectangle_intersect(r1, r2)
    assert expected_rec == actual_rec

def test_scenario3():
    r1 = pt.Rectangle(1, 0, 5, 4)
    r2 = pt.Rectangle(3, 9, 4, 4)
    actual_rec = pt.get_rectangle_intersect(r1, r2)
    assert actual_rec is None

def test_scenario4():
    r1 = pt.Rectangle(1, 0, 7, 4)
    r2 = pt.Rectangle(1, 0, 4, -4)
    expected_rec = pt.Rectangle(x=1, y=0, width=4, height=0)
    actual_rec = pt.get_rectangle_intersect(r1, r2)
    assert actual_rec == expected_rec

def test_scenario5():
    r1 = pt.Rectangle(1, 0, 7, 4)
    r2 = pt.Rectangle(1, 0, 7, 4)
    expected_rec = pt.Rectangle(x=1, y=0, width=7, height=4)
    actual_rec = pt.get_rectangle_intersect(r1, r2)
    assert actual_rec == expected_rec

def test_scenario6():
    r1 = pt.Rectangle(1, 0, 9, 6)
    r2 = pt.Rectangle(1, 0, -8, -3)
    expected_rec = pt.Rectangle(x=1, y=0, width=0, height=0)
    actual_rec = pt.get_rectangle_intersect(r1, r2)
    assert actual_rec == expected_rec

