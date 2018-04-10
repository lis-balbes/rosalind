#Rabbits and Recurrence Relations

#NOTE: recursion solution is much worse than O(n) and it's better to use for cycle next time
def offspring(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return offspring(n-1) + k*offspring(n-2)

with open('input.txt', 'r') as input:
    n, k = (int(i) for i in input.read().split())
    print(offspring(n))
