def offspring(n, k):
    generation = [1] + [0]*(k-1)
    for i in range(n-1):
        generation = [sum(generation[1:])] + generation[:-1]
    return sum(generation)

with open('input.txt', 'r') as input:
    n, k = (int(i) for i in input.read().split())
    print(offspring(n, k))

