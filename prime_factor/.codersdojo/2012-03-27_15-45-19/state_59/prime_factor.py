# Adapt the code to your code kata prime_factor.


def primes(nb):
    print("nb = %s" % nb)
    results = []
    if nb == 1:
        return results
    for i in range(2, nb+1):
        if nb < i:
            return results
        if nb % i == 0:
            results.append(i)
            new_nb = int(nb / i)
            results.extend(primes(new_nb))
            return results


def test_primes_1():
    assert primes(1) == []

def test_primes_2():
    assert primes(2) == [2]

def test_primes_3():
    assert primes(3) == [3]

def test_primes_4():
    assert primes(4) == [2, 2]

def test_primes_5():
    assert primes(5) == [5]

def test_primes_6():
    assert primes(6) == [2, 3]
