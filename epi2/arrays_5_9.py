import math


def get_primes(number):
    primes = []
    if number >= 2:
        primes = [2]
        for i in range(3, number + 1):
            is_prime = True
            p = 0
            while primes[p] <= math.sqrt(i):
                if i % primes[p] == 0:
                    is_prime = False
                    break
                p += 1

            if is_prime:
                primes.append(i)

    return primes


def get_primes_s(n):
    ''' Get primes with sieving '''
    primes = []

    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)

        for i in range(p, n + 1, p):
            is_prime[i] = False

    return primes


