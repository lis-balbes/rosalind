#Counting nucleotides in DNA

with open('input.txt', 'r') as input:
    dna = input.read()
    print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))
    # count() surprisingly works faster than "naive" algorithm with dictionary