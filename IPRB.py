# Mendel's First Law
# k - AA, m - Aa, n - aa

def probability(k, m, n):
    prob_aa_aa = float((n / (k + m + n)) * ((n - 1) / (k + m + n - 1)))
    prob_Aa_Aa = float((m / (k + m + n)) * ((m - 1) / (k + m + n - 1)))
    prob_Aa_aa = float((m / (k + m + n)) * (n / (k + m + n - 1)))*2
    return (1 - prob_aa_aa - prob_Aa_Aa / 4 - prob_Aa_aa / 2)


with open('input.txt', 'r') as input:
    k, m, n = (int(i) for i in input.read().split())
    print(probability(k, m, n))
