import multiprocessing
pattern = "*.gz"
combined = Counter()
with multiprocessing.Pool() as workers:
    result_iter = workers.imap_unordered(
        analysis,glob.glob(pattern)
    )
    for result in result_iter:
        combined.update(result)
