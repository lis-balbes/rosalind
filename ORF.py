rna_codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
    "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

from RNA import transcribeDnaToRna
from REVC import reverseComplement


def orf(rna):
    protein_s = 'M'

    for i in range(0, len(rna), 3):
        triplet = rna[i:i + 3]
        if len(triplet) < 3:
            return False
        if rna_codon_table[triplet] == "STOP":
            return protein_s
        protein_s += rna_codon_table[triplet]
    return False


with open('input.txt', 'r') as input:
    inp = input.read().split()
    dna = ''
    for i in inp[1:]:
        dna += i

    rna = transcribeDnaToRna(dna)

    proteins = set()
    n = len(rna)

    # For every frame compare it with start, if true - try to find stop and translate the rest of rna
    for i in range(n - 3):
        codone = rna[i:i + 3]
        if rna_codon_table[codone] == 'M':
            protein_string = orf(rna[i + 3: n])
            if protein_string:
                proteins.add(protein_string)

    # Same for reverse complement
    dna_reverse = reverseComplement(dna)
    rna_reverse = transcribeDnaToRna(dna_reverse)

    k = len(rna_reverse)

    for j in range(k - 3):
        codone = rna_reverse[j:j + 3]
        if rna_codon_table[codone] == 'M':
            protein_string = orf(rna_reverse[j + 3: n])
            if protein_string:
                proteins.add(protein_string)

    print('\n'.join(proteins))
