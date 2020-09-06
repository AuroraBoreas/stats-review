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
import math
from typing import Tuple
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

class WishCoin:
    def __init__(self) -> None:
        self.stat = 1 / 2

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

    def head_prob(self, heads: int, flip_times: int) -> float:
        if flip_times < 1 or heads > flip_times:
            raise ValueError('flip times must be >= 1. heads must be <= flip_times')
        if not heads:
            return (self.stat) ** flip_times    # all tails
        else:
            # CNM, i have to learn possibility theroem .. fml ..
            return (math.factorial(flip_times) / (math.factorial(heads) * math.factorial(flip_times - heads))) * self.stat ** flip_times


if __name__ == "__main__":
    ns = [10, 20, 40, 80, 100, 1000, 10_000, 100_000]
    t  = 3
    fmt = '{:0>2} tries, flipped coin {} times, heads={}, tail={}, heads ratio={:.2f}, tail ratio={:.2f}'
    for n in ns:
        for i in range(t):
            wc = WishCoin()
            ht = wc.flip(n)
            logging.debug(fmt.format(i+1, n, ht.heads, ht.tail, ht.hratio, ht.tratio))
        logging.debug(f'{"-" * 20}')

    X = 1
    f = 5
    wc = WishCoin()
    hp = wc.head_prob(X, f)
    logging.debug('head prob = {}'.format(hp))