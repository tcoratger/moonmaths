# Write a program to find the prime factors of a number
def primeFactors(n):
    while n % 2 == 0:
        print(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(n**0.5) + 1, 2):
        # while i divides n , print i and divide n
        while n % i == 0:
            print(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


n = 89
primeFactors(n)
