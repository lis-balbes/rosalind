max_gc_name = ''
max_gc_value = 0

def count_gc(dna):
    result = 0.0
    for i in dna:
        if i == 'G' or i == 'C':
            result += 1
    return 100*result/len(dna)

with open('input.txt', 'r') as input:
    inp = input.read().split()
    dna = dict()
    i = 0
    key = ''

    # Read input into a dictionary
    while i < len(inp):
        if inp[i].startswith('>'):
            key = inp[i][1:]
            dna[key] = ''
            i += 1
        else:
            dna[key] += inp[i]
            i += 1

    print(dna)

    # Iterate through dictionary and replace dna strings with their GC-content
    for k, v in dna.items():
        dna[k] = count_gc(v)
        if dna[k] > max_gc_value:
            max_gc_name = k
            max_gc_value = dna[k]

    print(max_gc_name, max_gc_value)