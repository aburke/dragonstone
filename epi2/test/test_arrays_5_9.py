import epi2.arrays_5_9 as arr

def test_scenario1():
    primes = arr.get_primes(18)
    expected_primes = [2, 3, 5, 7, 11, 13, 17]
    assert primes == expected_primes

def test_scenario2():
    primes = arr.get_primes(1)
    expected_primes = []
    assert primes == expected_primes

def test_scenario3():
    primes = arr.get_primes(2)
    expected_primes = [2]
    assert primes == expected_primes

def test_scenario4():
    primes = arr.get_primes_s(18)
    expected_primes = [2, 3, 5, 7, 11, 13, 17]
    assert primes == expected_primes

def test_scenario5():
    primes = arr.get_primes_s(1)
    expected_primes = []
    assert primes == expected_primes

def test_scenario6():
    primes = arr.get_primes_s(2)
    expected_primes = [2]
    assert primes == expected_primes