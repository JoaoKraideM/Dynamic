#1 faça uma função recursiva usando fatorial
import functools

def fatorialsemm(n, con):
    if n == 0:
        con = con + 1
        print(con)
        return 1
    else:
        return n * fatorialsemm(n-1, con + 1)


@functools.cache
def fatorial(n):
    global c
    if n == 0:
        c += 1
        return 1
    else:
        c += 1
        return n * fatorial(n-1)
c = 0

@functools.cache
def escrevearquivo(x):
    with open("saida.txt", "a") as f:
        f.write(f"{x}\n")
    return x


print(fatorialsemm(5, 0))
print(fatorial(5), c)

escrevearquivo(fatorial(5))


d = 0
@functools.cache
def somanumeros(x):
    global d
    if x < 10:
        d += 1
        return x
    else:
        d += 1
        return x % 10  + somanumeros(x // 10)


print(somanumeros(144), d)

e = 0
def somanumerossemm(x):
    global e
    if x < 10:
        e += 1
        return x
    else:
        e += 1
        return x % 10 + somanumerossemm(x//10)


g = 0
@functools.cache
def tribonnaci(x):
    global g
    if x == 0:
        g += 1
        return 0
    elif x == 1:
        g+=1
        return 0
    elif x == 2:
        g+=1
        return 1
    else:
        g += 1
        return tribonnaci(x - 1) + tribonnaci(x - 2) + tribonnaci(x - 3)


print(tribonnaci(35))


@functools.cache
def parimpar(x):
    if x % 10 == 0:
        return True
    else:
        return False

print(parimpar(10))




def conta_letra(n, c):
    if not n:
        return 0
    elif n[0] == c:
        return 1 + conta_letra(n[1::], c)
    else:
        return 0 + conta_letra(n[1::], c)


print(conta_letra('banana', 'a'))