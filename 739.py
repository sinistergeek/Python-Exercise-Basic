all = repeat(0)
subset = cycle(range(100))
choose = lambda rule: (x == 0 for x  in rule)

def randseq(limit):
    while True:
        yield random.randrange(limit)
randomized = randseq(100)
