import time

from matplotlib import pyplot as plt


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_memo(n):
    if n in cache:
        return cache[n]
    if n == 1 or n == 2:
        cache[n] = n
        return 1
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return fib(n-1) + fib(n-2)

cache = {}

import functools
@functools.cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

@functools.cache
def escreve_arquivo(x):
    with open("sainda.txt", "a") as f:
        f.write(f"{x}\n")
    return x

escreve_arquivo(1)