def is_prime(number):
    if number <= 1:
        return False

    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True

def get_primes(n_start, n_end):
    prime_list = []
    for number in range(n_start, n_end):
        if is_prime(number):
            prime_list.append(number)
    return prime_list

def lucas_lehmer(p):
    ll_seq = [4]
    if p>2:
        for i in range(1, (p-2)+1):
            n_i = ((ll_seq[i-1]) ** 2 - 2) % ((2 ** p) - 1)
            ll_seq.append(n_i)
    return ll_seq


def ll_prime(p):
    if lucas_lehmer(p)[-1] == 0:
        return 1
    return 0

ll_list = []
for p in get_primes(3,65):
    ll_list.append(ll_prime(p))

mersenne_primes = list(zip(get_primes(3,65), ll_list))

print(mersenne_primes)

