# Counting Point Mutations
# Given two strings s and t of equal length, count the Hamming distance between s and t

def hamming(s, t):
    result = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            result += 1
    return result


with open('input.txt', 'r') as input:
    s, t = input.read().split()
    print(hamming(s, t))
