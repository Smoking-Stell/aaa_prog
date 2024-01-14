from typing import TypeVar, Sequence, Callable, Generator, List

T = TypeVar('T')
U = TypeVar('U')


class Seq:
    def __init__(self, sequence: Sequence[T]):
        self.sequence = sequence

    def map(self, func: Callable[[T], U]) -> "Seq[U]":
        return Seq((func(x) for x in self.sequence))

    def filter(self, func: Callable[[T], bool]) -> 'Seq[T]':
        return Seq((x for x in self.sequence if func(x)))

    def take(self, n: int) -> List[T]:
        return list(self._take_generator(n))

    def _take_generator(self, n: int) -> Generator[T, None, None]:
        count = 0
        for item in self.sequence:
            if count >= n:
                break
            yield item
            count += 1


seq = Seq([1, 2, 3, 4, 5, 6, 7, 8])
filtered_seq = seq.map(lambda x: x ** 2).filter(lambda x: x % 2 == 0)

result = filtered_seq.take(3)

print(result)