import epi2.strings_6_7 as st

def test_scenario1():
    expected = ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
    actual = st.find_paths('23*')
    assert expected == actual

def test_scenario2():
    expected = ['WG', 'WH', 'WI', 'XG', 'XH', 'XI', 'YG', 'YH', 'YI', 'ZG', 'ZH', 'ZI']
    actual = st.find_paths('9#4')
    assert expected == actual

def test_scenario3():
    expected = ['J', 'K', 'L']
    actual = st.find_paths('105')
    assert expected == actual

def test_scenario4():
    expected = ['DPM', 'DPN', 'DPO', 'DQM', 'DQN', 'DQO', 'DRM', 'DRN', 'DRO', 'DSM', 'DSN', 'DSO', 'EPM', 'EPN', 'EPO', 'EQM', 'EQN', 'EQO', 'ERM', 'ERN', 'ERO', 'ESM', 'ESN', 'ESO', 'FPM', 'FPN', 'FPO', 'FQM', 'FQN', 'FQO', 'FRM', 'FRN', 'FRO', 'FSM', 'FSN', 'FSO']
    actual = st.find_paths('376')
    assert expected == actual

def test_scenario5():
    expected = ['']
    actual = st.find_paths('10*#')
    assert expected == actual