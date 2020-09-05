"""
a simple module calculates properties of a group of data.

it has the following functionalities
- calculate length of the group of data
- center tendency
- range
- midrange

about
@ZL, 20200903
"""

from typing import Union, Tuple, List
import collections

class SimpleStatistics:
    def __init__(self, seq: List[Union[int, float]]) -> None:
        self.seq = seq
        
    def __len__(self) -> Union[int, float]:
        return len(self.seq)

    def get_sum(self) -> Union[int, float]:
        total = 0
        for i in self.seq:
            total += i
        return total

    def mean(self) -> Union[int, float]:
        return self.get_sum() / len(self.seq)

    def median(self) -> Union[int, float]:
        sorted_seq = sorted(self.seq)
        middle     = int(len(self.seq) / 2)
        if len(self.seq) % 2:
            return sorted_seq[middle - 1]
        else:
            return (sorted_seq[middle - 1] + sorted_seq[middle]) / 2

    def mode(self) -> Union[int, float]:
        c = collections.Counter(self.seq)
        return c.most_common(1)[0][0]

    def _range(self) -> Union[int, float]:
        return max(self.seq) - min(self.seq)
    
    def _midrange(self) -> float:
        return max(self.seq) + min(self.seq) / 2

class varSimpleStatistics(SimpleStatistics):
    def variance(self) -> float:
        if self.seq:
            m = self.mean()
            r = [(i - m)**2 for i in self.seq]
            return sum(r) / len(self.seq)
        else:
            raise ValueError('empty squence is Not allowed')

    def pstdvar(self) -> float:
        """
        NOTE: population standard variance
        """
        return self.variance() ** .5

    def sstdvar(self) -> float:
        """
        NOTE: sample standard variance
        """
        if self.seq:
            m = self.mean()
            r = [(i - m)**2 for i in self.seq]
            return (sum(r) / (len(self.seq) - 1)) ** .5
        else:
            raise ValueError('empty squence is Not allowed')