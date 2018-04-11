# Transcribing DNA into RNA


def transcribeDnaToRna(dna):
    rna = dna.replace('T', 'U')
    return rna

'''
with open('input.txt', 'r') as input:
    dna = input.read()
    print(dna)
    print(transcribeDnaToRna(dna))
'''