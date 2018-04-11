from REVC import reverseComplement

with open('input.txt', 'r') as input:
    inp = input.read().split()
    dna = ''
    for i in inp[1:]:
        dna += i

    for i in range(len(dna)):
        for j in range(4, 13):
            dna_to_check = dna[i:i+j]
            if len(dna_to_check) == j and dna_to_check == reverseComplement(dna_to_check):
                print(str(i+1) + " " + str(j))