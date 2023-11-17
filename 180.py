dna = 'ACCGXXCXXGTTACTGGGCXTTGT'
sequences = dna.split('X')
sequences.sort(key=len,reverse=True)

def not_empty(x):
    return len(x) > 0

print(sequences)
sequences = list(filter(lambda x: len(x) > 0,sequences))
print(sequences)
