def lucas_lehmer(p):
    ll_seq = [4]
    if p>2:
        for i in range(1, (p-2)+1):
            n_i = ((ll_seq[i-1]) ** 2 - 2) % ((2 ** p) - 1)
            ll_seq.append(n_i)
    return ll_seq

print(lucas_lehmer(17))
