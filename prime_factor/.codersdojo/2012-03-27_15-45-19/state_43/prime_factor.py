# Adapt the code to your code kata prime_factor.


def primes(nb):
    results = []
    print("** test %s" % nb)
    for i in range(2, nb+1):
        if nb < i:
            return results
        if nb % i == 0:
            results.append(i)
            new_nb = int(nb / i)
            print(primes(new_nb))
            #return results.extend(primes(new_nb))


def test_primes_1():
    assert primes(1) == []

def test_primes_2():
    assert primes(2) == [2]

def test_primes_3():
    assert primes(3) == [3]

def test_primes_4():
    assert primes(4) == [2, 2]
