#Expected value for offspring displaying the dominant phenotype

def expected_value(pairs):
    return pairs[0]*2 + pairs[1]*2 + pairs[2]*2 + pairs[3]*2*0.75 + pairs[4]*2*0.5

with open('input.txt', 'r') as input:
    pairs = list((int(i) for i in input.read().split()))
    print(expected_value(pairs))