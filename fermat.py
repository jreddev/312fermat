import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.   
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
    # You will need to implement this function and change the return value.   
    return 0.0


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 0.0


def fermat(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    while k > 0:
        mod = mod_exp(random.randint(2, (N - 1)), N-1, N)
        if mod != 1:
            return 'composite'
        k -= 1
    return 'prime'


def miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    return 'composite'
