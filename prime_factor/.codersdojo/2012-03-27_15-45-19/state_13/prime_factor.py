# Adapt the code to your code kata prime_factor.


def primes(nb):
    primes = []
    for i in range(2, nb+1):
        print(i)
        if nb < i:
            break
        if nb % i == 0:
            print(i)
            primes.append(i)
    return primes


def test_primes_1():
    assert primes(1) == []

def test_primes_2():
    assert primes(2) == [2]

def test_primes_3():
    assert primes(3) == [3]
