number = 3
primes = [2]

with open("prime_numbers.txt", "w") as file:
    while 1:
        for prime in primes:
            if not number % prime:
                break
        else:
            primes.append(number)
            print("Found prime number:", number)
            file.write(str(number) + "\n")
        number += 1