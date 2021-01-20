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


def mersennes(n_start,n_end):
    mersenne_list = []
    my_list=get_primes(n_start, n_end)
    for i in my_list:
        x = 2**i - 1
        mersenne_list.append(x)
    return mersenne_list

mersennes= mersennes(3,65)
print(mersennes)