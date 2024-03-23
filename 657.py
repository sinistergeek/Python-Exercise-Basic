def sumr(seq):
    if len(seq) == 0: return 0
    return seq[0] + sumr(seq[1:])
