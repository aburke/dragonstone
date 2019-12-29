import epi2.strings_6_8 as st

def test_scenario1():
    expected = '1'
    acutal = st.look_n_say(0)
    assert expected == acutal

def test_scenario2():
    expected = '11'
    acutal = st.look_n_say(1)
    assert expected == acutal

def test_scenario3():
    expected = '13112221'
    actual = st.look_n_say(6)
    assert expected == actual