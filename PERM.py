#Count and print permutation for {1, 2, ..., n}

#Cheaty-easy way - use functions from standard library
'''
import itertools
import math

with open('input.txt', 'r') as input:
    n = int(input.read())
    N = list(range(1, n + 1))
    print(math.factorial(n))
    for i in list(itertools.permutations(N, n)):
        print(i)
'''

#Heap's algorithm

def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def perm(N, n):
    if n == 1: yield N #returning generator
    else:
        for i in range(n-1):
            for hp in perm(N, n-1): yield hp
            j = 0 if (n % 2) == 1 else i
            N[j],N[n-1] = N[n-1],N[j] #if n is odd - swap first and last, else - swap current and last
        for hp in perm(N, n-1): yield hp



with open('input.txt', 'r') as input:
    n = int(input.read())
    N = list(range(1, n + 1))
    print(fact(n))
    for i in perm(N,n):
        for j in i:
            print(j, end = " ")
        print()