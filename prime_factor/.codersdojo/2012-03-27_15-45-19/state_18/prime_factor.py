# Adapt the code to your code kata prime_factor.


def primes(nb):
    primes = []
    for i in range(2, nb+1):
        print(i, nb)
        if nb < i:
            break
        if nb % i == 0:
            primes.append(i)
            primes.append(primes(nb /= i))
    return primes


def test_primes_1():
    assert primes(1) == []

def test_primes_2():
    assert primes(2) == [2]

def test_primes_3():
    assert primes(3) == [3]

def test_primes_4():
    assert primes(4) == [2, 2]
