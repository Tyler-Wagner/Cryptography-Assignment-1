"""
Code written by Tyler Wagner
Used by: Tyler Wager, Jordan Ricks, Alexis Davis
"""

import time


def main():
    prime1 = int(input("Enter a number: "))
    prime2 = int(input("Enter a number: "))

    # get the answer and the time it took to multiply from the multiply method
    primeAnswer, multiplyTime = multiply(prime1, prime2)

    print(primeAnswer)

    # open the output file
    outFile = open("outputFile.txt", "w")

    # cast the multiplyTime flat to a string
    strMultTime = str(multiplyTime)

    # Write to file
    outFile.write(f"Time to multiply: {strMultTime}")

    if _isPrime(primeAnswer) is True:
        factor(primeAnswer)

    else:
        print(f"{primeAnswer} is not prime factoring now")
        factor(primeAnswer)

    # Get the factor time and the list of factors form the factor method
    results = factor(primeAnswer)
    final, factorTime = results[:-1], results[-1]
    print(final)

    # cast the factorTime to a string
    strFactorTime = str(factorTime)

    # Write the output to the file
    outFile.write(f"\nTime to factor: {strFactorTime}")

    outFile.close()


def multiply(prime1, prime2):
    startTimer = time.perf_counter()
    primeAnswer = prime1 * prime2
    stopTimer = time.perf_counter()
    finTimer = stopTimer - startTimer
    print(f"Calculated the two prime numbers in {finTimer:0.10f} seconds")
    return primeAnswer, finTimer


def factor(primeAnswer, divisor=2):
    factors = []
    startFacTimer = time.perf_counter()
    while primeAnswer > 1 and divisor * divisor <= primeAnswer:
        if primeAnswer % divisor == 0:
            factors.append(divisor)
            return factors + factor(primeAnswer // divisor, divisor)
        divisor += 1

        if primeAnswer > 1:
            factors.append(primeAnswer)

        # Only uncomment the line before this if you need to check for errors
        # print(divisor)
    stopFacTimer = time.perf_counter()
    finTimer = stopFacTimer - startFacTimer
    print(f"Finished in {finTimer: .04f} seconds")
    return factors + [finTimer]


def _isPrime(primeAnswer):
    if primeAnswer <= 1:
        return False
    if primeAnswer <= 3:
        return True
    if primeAnswer % 2 == 0 or primeAnswer % 3 == 0:
        return False
    i = 5
    while i * i <= primeAnswer:
        if primeAnswer % i == 0 or primeAnswer % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    main()
