

def nthPrime(n : int) -> int:
    primes = [2]
    number = 3
    while len(primes) < n:
        if 0 not in {(number % prime) for prime in primes}:
            primes.append(number)
        number += 1
    return primes[-1]
