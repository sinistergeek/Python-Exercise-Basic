from collections.abc import Sequence
from pymonad import curry

@curry
def myreduce(function,iterable_or_sequence):
    if isinstance(iterable_or_sequence,Sequence):
        iterator = iter(iterable_or_sequence)
    else:
        iterator = iterable_or_sequence 
    s = next(iterator)
    for v in iterator:
        s = function(s,v)
    return s
