import re
import requests

with open('input.txt', 'r') as input:
    uniProtList = input.read().split()
    for i in uniProtList:
        print(i)

        # Get protein
        r = requests.get('http://www.uniprot.org/uniprot/' + i + '.fasta')
        prot = r.text

        # Convert protein from fasta to simple string
        prot = ''.join(prot.splitlines()[1:])

        # Count
        l = len(prot)
        for i in range(l):
            if prot[i - l] == 'N' and (prot[(i+1) - l] != 'P') and (prot[(i+2) - l] == 'S' or prot[(i+2) - l] == 'T') and (prot[(i+3) - l] != 'P'):
                print(i + 1, end=' ')
        print()