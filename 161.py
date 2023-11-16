def filter_and_sort_sequences(sequence):
    valid_sequences = ["".join(filter(lambda x: x in "ACTG",segment)) for segment in sequence.split('X') if any(c in "ACTG" for c in segment)]
    sorted_sequences = sorted(valid_sequences,key=len,reverse=True)
    return sorted_sequences

sequence = 'ACCGXXCXXGTTACTGGGCXTTGT'
result = filter_and_sort_sequences(sequence)
print(result)
