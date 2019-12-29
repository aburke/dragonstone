import epi2.arrays_5_5 as arrs

def test_scenario1():
    e_res = [2, 3, 5, 7, 11, 13]
    t_arr = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    res = arrs.remove_duplicates_from_sorted(t_arr)
    assert e_res == res

def test_scenario2():
    e_res = [2]
    t_arr = [2, 2, 2, 2]
    res = arrs.remove_duplicates_from_sorted(t_arr)
    assert e_res == res

def test_scenario3():
    e_res = [1]
    t_arr = [1]
    res = arrs.remove_duplicates_from_sorted(t_arr)
    assert e_res == res

def test_scenario4():
    e_res = [9, 11, 12, 15]
    t_arr = [9, 9, 9, 9, 11, 12, 12, 12, 15, 15]
    res = arrs.remove_duplicates_from_sorted(t_arr)
    assert e_res == res