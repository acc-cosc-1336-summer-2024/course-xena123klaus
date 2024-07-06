def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("Strings muse be same length")
    
    distance = 0
    for ch1, ch2 in zip(dna1, dna2):
        if ch1 != ch2:
            distance += 1
    return distance

def get_dna_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_dna = dna[::-1]
    complement_dna = ''.join(complement[ch] for ch in reversed_dna)
    return complement_dna
