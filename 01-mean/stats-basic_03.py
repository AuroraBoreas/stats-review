"""

concept : random variable
symbol  : capital X
usage   : simulates real world factor.

    |- 1 if rain
X = |
    |- 0 if no rain

or flipping a coin

    |- 1 if heads
X = |
    |- 0 if tail

R.V.
|-- discrete
|-- contious
(yeah, just like concept in calculus)

concept: probability

concept: possibility density
concept: possibility distribution function

"""
import random
import collections
import logging
from typing import Tuple
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class WishCoin:
    def __init__(self):
        self.sides = 2

    def flip(self, n: int) -> Tuple[int, int, float]:
        heads, tail = 1, 0
        ht = [heads, tail]
        if n < 1:
            raise ValueError('flip times must be >= 1')
        else:
            r = []
            c = collections.namedtuple('CoinHeadsTailCount', 'heads tail hratio tratio')
            for _ in range(n):
                r.append(random.choice(ht))
        return c(r.count(heads), r.count(tail), r.count(heads) / len(r), r.count(tail) / len(r))

ns = [10, 20, 40, 80, 100, 1000, 10_000, 100_000]
t  = 3
fmt = '{:0>2} tries, flipped coin {} times, heads={}, tail={}, heads ratio={:.2f}, tail ratio={:.2f}'
for n in ns:
    for i in range(t):
        wc = WishCoin()
        ht = wc.flip(n)
        logging.debug(fmt.format(i+1, n, ht.heads, ht.tail, ht.hratio, ht.tratio))
    logging.debug(f'{"-" * 20}')