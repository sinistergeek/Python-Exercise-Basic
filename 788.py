import multiprocessing 
pattern = "*.gz"
combined = Counter()
with multiprocessing.Pool() as workers:
    results = workers.map_async(analysis,glob.glob(pattern))
    data = results.get()
    for c in data:
        combined.update(c)
