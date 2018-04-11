#Complementing a Strand of DNA

def reverseComplement(dna):
    compl = ""
    for i in dna[::-1]:
        if i == 'A':
            compl += 'T'
        elif i == 'T':
            compl += 'A'
        elif i == 'C':
            compl += 'G'
        elif i == 'G':
            compl += 'C'
    return compl

'''
with open('input.txt', 'r') as input:
    dna = input.read()
    print(reverseComplement(dna))
'''