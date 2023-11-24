from collections.abc import Iterator,Iterable
from types import GeneratorType

print(issubclass(GeneratorType,Iterator))
print(issubclass(Iterator,Iterable))
