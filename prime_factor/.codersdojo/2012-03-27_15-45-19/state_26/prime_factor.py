# Adapt the code to your code kata prime_factor.


def primes(nb):
    primes = []
    for i in range(2, nb+1):
        if nb < i:
            return primes
        if nb % i == 0:
            primes.append(i)
            print(primes)
            print(primes)
            print("*" * 20)
            return primes.extend(primes(nb / i))


def test_primes_1():
    assert primes(1) == []

def test_primes_2():
    assert primes(2) == [2]

def test_primes_3():
    assert primes(3) == [3]

def test_primes_4():
    assert primes(4) == [2, 2]
