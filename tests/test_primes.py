from spielwiese import primes


def test_nthPrime():
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    actual = []
    for n in range(1, 10 + 1):
        actual.append(primes.nthPrime(n))
    assert expected == actual
