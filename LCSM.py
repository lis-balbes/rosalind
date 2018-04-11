def lcs(strings):
    strings_number = len(strings)
    len_first_string = len(strings[0])

    # Main idea - try all substrings from first string and check whether it is substring for another strings

    for i in range(len_first_string, 0, - 1): #length of substring
        for j in range(len_first_string - i + 1): # number of symbols in substring of this length
            candidate = strings[0][j:(j+i)]
            found = [False] * (strings_number - 1) #array showing if substring is found in corresponding string
            for stringNumber in range(1, strings_number):
                found[stringNumber - 1] = strings[stringNumber].find(candidate) > 0
                if not found[stringNumber - 1]:
                    break
            if all(f for f in found):
                return candidate

with open('input.txt', 'r') as input:
    # Read input into a dictionary
    inp = input.read().split()
    dna = dict()
    i = 0
    key = ''

    while i < len(inp):
        if inp[i].startswith('>'):
            key = inp[i][1:]
            dna[key] = ''
            i += 1
        else:
            dna[key] += inp[i]
            i += 1

    print(lcs(list(dna.values())))