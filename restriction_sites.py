# Function to get the reverse complement of a DNA sequence
def reverse_complement(seq):
    complement = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(complement[base] for base in reversed(seq))

#Function to find all reverse palindromes between length 4 and 12
def find_reverse_palindromes(dna):
    results = []
    for i in range(len(dna)):
        for length in range(4, 13): # length from 4 to 12
            if i + length <= len(dna):
                sub_seq = dna[i:i+length]
                if sub_seq == reverse_complement(sub_seq):
                    results.append((i + 1, length)) # 1-based index
    return results

# Sample FASTA input
fasta = """>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT"""

# Parse FASTA
lines = fasta.strip().split('\n')
dna_seq = ''.join(line for line in lines if not line.startswith('>'))

# Find and print reverse palindromes
for pos, length in find_reverse_palindromes(dna_seq):
    print(pos, length)
