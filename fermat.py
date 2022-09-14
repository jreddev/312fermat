import random

def prime_test(N, k):
    return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, int(y/2), N)
    if y % 2 == 0:
        r = (z * z) % N
        return r
    else:
        r = (x * z * z) % N
        return r


def fprobability(k):
    return 1 - (1 / (2**k))


def mprobability(k):
    return 1 - (1 / (4**k))


def fermat(N,k):
    while k > 0:
        mod = mod_exp(random.randint(2, (N - 1)), N-1, N)
        if mod != 1:
            return 'composite'
        k -= 1
    return 'prime'


def miller_rabin(N,k):
    while k > 0:
        root = N - 1
        a = random.randint(2, root)
        mod = mod_exp(a, root, N)
        if mod == 1:
            while mod == 1:
                root = (root / 2)
                if float.is_integer(root):
                    mod = mod_exp(a, root, N)
        if mod == (N - 1):
            return 'prime'
        else:
            return 'composite'

    return 'composite'