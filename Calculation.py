import time
import math

def main():
    prime1 = int(input("Enter a prime number: "))
    prime2 = int(input("Enter a prime number: "))

    primeAnswer = multiply(prime1, prime2)
    print (primeAnswer)

    factor(primeAnswer)




def multiply(prime1, prime2):
    startTimer = time.perf_counter()
    primeAnswer = prime1 * prime2
    stopTimer = time.perf_counter()
    print(f"Calculated the two prime numbers in {stopTimer - startTimer:0.10f} seconds")
    return primeAnswer



def factor(primeAnswer):
    factoredNumbers = []
    startFacTimer = time.perf_counter()
    for i in range(2, int(math.sqrt(primeAnswer))):
        isPrime = primeAnswer % i
        print(isPrime)
        if isPrime == 1 or isPrime == primeAnswer:
            print ("Prime number")
    stopFacTimer = time.perf_counter()

    print(f"Finished in {stopFacTimer - startFacTimer: .04f} seconds")
    print(factoredNumbers)
    


if __name__ == "__main__":
    main()