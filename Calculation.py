import time
import math

def main():
    prime1 = int(input("Enter a prime number: "))
    prime2 = int(input("Enter a prime number: "))

    primeAnswer = multiply(prime1, prime2)
    print (primeAnswer)

    final = factor(primeAnswer)
    print (final)


def multiply(prime1, prime2):
    startTimer = time.perf_counter()
    primeAnswer = prime1 * prime2
    stopTimer = time.perf_counter()
    print(f"Calculated the two prime numbers in {stopTimer - startTimer:0.10f} seconds")
    return primeAnswer


def factor(primeAnswer, divisor = 2):
    factors = []
    startFacTimer = time.perf_counter()
    while primeAnswer > 1 and divisor * divisor <= primeAnswer:
        if primeAnswer% divisor == 0:
            factors.append(divisor)
            return factors + factor(primeAnswer // divisor, divisor)
        divisor += 1
        print(divisor)
    stopFacTimer = time.perf_counter()
    print(f"Finished in {stopFacTimer - startFacTimer: .04f} seconds")


def _isPrime(primeAnswer):
    if primeAnswer <= 1:
        return False
    if primeAnswer <=3:
        return True
    if primeAnswer % 2 == 0 or primeAnswer % 3 == 0:
        return False
    i = 5
    while i * i <= primeAnswer:
        if primeAnswer % i == 0 or primeAnswer % (i + 2) == 0:
            return False
        i+= 6
    return True




if __name__ == "__main__":
    main()