"""
concept: smaple vs population

+-----------+-------------------------------+-------------------------------+
| diff      | sample                        | population                    |
+===========+===============================+===============================+
| what?     | part of population            | all                           |
+-----------+-------------------------------+-------------------------------+
| why?      | time/space/cost etc limits    | huge in real life             |
+-----------+-------------------------------+-------------------------------+
| how?      | random samling data to        | -                             |
|           | represent population          |                               |
+-----------+-------------------------------+-------------------------------+
| sum       | sum(1...n)                    | sum(1...N)                    |
+-----------+-------------------------------+-------------------------------+
| mean      | x-bar = sum(1...n)/n          | u = sum(1...N)/N              |
+-----------+-------------------------------+-------------------------------+
| variance  | s^2                           | σ^2                           |
+-----------+-------------------------------+-------------------------------+
| stdvar    | s = (sum(Xi-mean)/(n-1)) ^ .5 | σ = (sum(Xi-u)/N) ^ .5        |                 |
+-----------+-------------------------------+-------------------------------+

concept: dispersion

"""
import sys
sys.path.append('.')
from libraries.pkg.stats import SimpleStatistics, varSimpleStatistics
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')
from typing import Union

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
# assert variance1 == variance2, "variance of population Not equal"

stdvar1 = varSimpleStatistics(p1).pstdvar()
stdvar2 = varSimpleStatistics(p2).pstdvar()
logging.debug(f'population 1: standard variance = {stdvar1}')
logging.debug(f'population 2: standard variance = {stdvar2}')


p3  = [1, 2, 3, 8, 7]
ss3 = varSimpleStatistics(p3)
variance3 = ss3.variance()
stdvar3   = ss3.pstdvar()
logging.debug(f'population 3: variance = {variance3}')
logging.debug(f'population 3: population standard variance = {stdvar3}')