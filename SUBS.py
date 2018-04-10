#Find all positions of substring in string

with open('input.txt', 'r') as input:
    dna, substring = input.read().split()
    result = set()
    i = 0
    for i in range(len(dna)):
        position = dna.find(substring, i)
        if position != -1:
            result.add(position + 1)
    for i in sorted(result):
        print(i, end=" ")

#Elegant python solution:
'''
for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print i+1
'''