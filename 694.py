from collections.abc import Sequence
class ExpandingSequence(Sequence):
    def __init__(self, it):
        self.it = it
        self._cache =[]
    def __getitem__(self,index):
        while len(self._cache) <= index:
            self._cache.append(next(self.it))
        return self._cache[index]
    def __len__(self):
        return len(self._cache)

primes = ExpandingSequence(get_primes())
for _, p in zip(range(10),primes):
    print(p, end=" ")
