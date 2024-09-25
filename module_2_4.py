# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes, not_primes = [], []

for num in numbers:
    is_prime = True
    if num == 1:
        continue
    if num == 2:
        primes.append(num)
        continue
    list_ = list(range(2, num))
    for l in list_:
        if num % l == 0:
            is_prime = False
    if is_prime == False:
        not_primes.append(num)
    else:
        primes.append(num)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')