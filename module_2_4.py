
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False
not_prime = False
k_prime = 0
k_not_prime = 0
for i in numbers:
    for j in range(len(numbers)):

        if i % (j+1) == 0 and i != 1:
            is_prime = True
            k_prime += 1

        if i != 1 and i % (j+1) == 0 and i != 2:
            not_prime = True
            k_not_prime += 1

        if k_prime == 2 and k_not_prime > 2:
            break

    if is_prime and k_prime == 2:
        primes.append(i)


    if not_prime and k_not_prime > 2:
        not_primes.append(i)

    k_prime = 0
    k_not_prime = 0
    is_prime = False
    not_prime = False


print(primes)
print(not_primes)