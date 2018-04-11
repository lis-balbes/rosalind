# RNA Splicing

rna_codon_table = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
}

with open('input.txt', 'r') as input:
    inp = input.read().split()

    d = dict()
    i = 0
    key = ''

    # Read input into a dictionary
    while i < len(inp):
        if inp[i].startswith('>'):
            key = inp[i][1:]
            d[key] = ''
            i += 1
        else:
            d[key] += inp[i]
            i += 1

    dna = list(d.values())[0]
    intrones = list(d.values())[1:]

    print(dna)
    print(intrones)

    # In this task there was no need to have a list of exones, but maybe later we will
    # need to modify solution for alternative splicing - so it will be better to implement splitting by several delimiters
    # TODO: Do it. Later.

    # Remove intrones from dna
    dna_after_splicing = dna
    for introne in intrones:
        split = dna_after_splicing.split(sep=introne, maxsplit=1)
        dna_after_splicing = split[0] + split[1]
    print(dna_after_splicing)


    # Convert DNA to RNA
    rna = dna_after_splicing.replace('T', 'U')
    print(rna)

    #Translate RNA
    for i in range(0, len(rna), 3):
        triplet = rna[i:i+3]
        if rna_codon_table[triplet] == "STOP":
            break
        print(rna_codon_table[triplet], end="")