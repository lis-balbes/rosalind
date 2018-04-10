#Transcribing DNA into RNA

with open('input.txt', 'r') as input:
    dna = input.read()
    #strings are immutable in python!
    rna = dna.replace('T', 'U')
    print(dna)
    print(rna)

