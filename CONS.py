'''
Notes: this task should be easier with numpy
TODO: try it later
'''

with open('input.txt', 'r') as input:

    # Read input as dictionary and extract list dna of strings
    inp = input.read().split()
    d = dict()
    i = 0
    key = ''
    while i < len(inp):
        if inp[i].startswith('>'):
            key = inp[i][1:]
            d[key] = ''
            i += 1
        else:
            d[key] += inp[i]
            i += 1
    dna = list(d.values())

    # Count profile
    dna_len = len(dna[0])
    dna_count = len(dna)

    profile = {
        'A': [0]*dna_len,
        'C': [0]*dna_len,
        'G': [0]*dna_len,
        'T': [0]*dna_len
    }

    for i in range(dna_count):
        for j in range(dna_len):
            profile[dna[i][j]][j] += 1

    # Count consensus
    # TODO: think of the way to combine these steps
    consensus = ''
    max_nucleotide = ''
    max_nucleotide_count = 0
    for i in range(dna_len):
        for k, v in profile.items():
            if v[i] >= max_nucleotide_count:
                max_nucleotide = k
                max_nucleotide_count = v[i]
        consensus += max_nucleotide
        max_nucleotide = ''
        max_nucleotide_count = 0

    print(consensus)

    for k, v in profile.items():
        print(k + ': ' + ' '.join((str(i) for i in v)))