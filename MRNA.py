#Inferring mRNA from Protein

proteins_to_rna = {
    'A': 4,
    'R': 6,
    'N': 2,
    'D': 2,
    'C': 2,
    'Q': 2,
    'E': 2,
    'G': 4,
    'H': 2,
    'I': 3,
    'L': 6,
    'K': 2,
    'M': 1,
    'F': 2,
    'P': 4,
    'S': 6,
    'T': 4,
    'W': 1,
    'Y': 2,
    'V': 4,
    'STOP': 3
}

with open('input.txt', 'r') as input:
    protein_string = input.read().strip()
    result = 1
    for i in protein_string:
        result = (result * proteins_to_rna[i]) % 1000000
    result = (result * proteins_to_rna['STOP']) % 1000000
    print(protein_string)
    print(result)