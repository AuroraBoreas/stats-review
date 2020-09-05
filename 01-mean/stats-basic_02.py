"""
concept: smaple vs population

+-----------+-------------------------------+-----------------------+
| diff      | sample                        | population            |
+===========+===============================+=======================+
| what?     | part of population            | all                   |
+-----------+-------------------------------+-----------------------+
| why?      | time/space/cost etc limits    | huge in real life     |
+-----------+-------------------------------+-----------------------+
| how?      | random samling data to        | -                     |
|           | represent population          |                       |
+-----------+-------------------------------+-----------------------+
| sum       | sum(1...n)                    | sum(1...N)            |
+-----------+-------------------------------+-----------------------+
| mean      | x-bar = sum(1...n)/n          | u = sum(1...N)/N      |
+-----------+-------------------------------+-----------------------+

concept: dispersion

"""
import sys
sys.path.append('.')
from libraries.pkg.stats import SimpleStatistics
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')
from typing import Union

class varSimpleStatistics(SimpleStatistics):
    def variance(self) -> float:
        if self.seq:
            m = self.mean()
            r = [(i - m)**2 for i in self.seq]
            return sum(r) / len(self.seq)
        else:
            raise ValueError('empty squence is Not allowed')

p1 = [2, 2, 3, 3]
p2 = [0, 0, 5, 5]

u1 = SimpleStatistics(p1).mean()
u2 = SimpleStatistics(p2).mean()
logging.debug(f'population 1: mean = {u1}')
logging.debug(f'population 2: mean = {u2}')
assert u1 == u2, 'mean of population Not equal'

variance1 = varSimpleStatistics(p1).variance()
variance2 = varSimpleStatistics(p2).variance()
logging.debug(f'population 1: variance = {variance1}')
logging.debug(f'population 2: variance = {variance2}')
assert variance1 == variance2, "variance of population Not equal"