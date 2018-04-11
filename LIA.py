import math

k, N = (int(i) for i in input().split())

generation_size = 2 ** k
p_reverse = 0.0
for i in range(N - 1, -1, -1):  # counting probability to have i offsprings, where i < N
    p_reverse += math.factorial(generation_size) / (math.factorial(i) * math.factorial(generation_size - i)) * (
        (0.25) ** i) * ((0.75) ** (generation_size - i))
p = 1 - p_reverse

print(p)