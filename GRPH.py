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
    print(d)

    values = list(d.values())
    for k, v in d.items():
        for key, value in d.items():
            if v != value and v[-3:] == value[:3]:
                print(k + " " + key)