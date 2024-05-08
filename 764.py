import random
indices = list(range(len(y)))
random.shuffle(indices)
x = [None] * len(y)
for k in indices:
    x[k] = func(y[k])
