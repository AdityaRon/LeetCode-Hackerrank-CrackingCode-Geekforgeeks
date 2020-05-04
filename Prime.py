def isPrime(n):
    if n < 2:
        return 0
    Primes = [1] * n
    Primes[0] = Primes[1] = 0
    for i in range(2, int(n**0.5)+1):
        if Primes[i] == 1:
            Primes[i*i:n:i] = [0]* len(Primes[i*i:n:i])
    return sum(Primes)
