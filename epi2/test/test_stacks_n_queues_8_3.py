import epi2.stacks_n_queues_8_3 as sq

def test_scenario1():
    well_formed = sq.is_well_formed('()')
    assert well_formed
    
def test_scenario2():
    well_formed = sq.is_well_formed('[)')
    assert not well_formed

def test_scenario3():
    well_formed = sq.is_well_formed('[({[([])]})]')
    assert well_formed

def test_scenario4():
    well_formed = sq.is_well_formed('([{}]]')
    assert not well_formed

def test_scenario5():
    well_formed = sq.is_well_formed(')')
    assert not well_formed

def test_scenario6():
    well_formed = sq.is_well_formed('[')
    assert not well_formed

def test_scenario7():
    well_formed = sq.is_well_formed('')
    assert well_formed

def test_scenario8():
    well_formed = sq.is_well_formed('}{')
    assert not well_formed