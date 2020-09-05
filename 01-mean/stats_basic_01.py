"""
? Q: Find the `mean`, `median`, and `mode` of the following set of numbers:
     23, 29, 20, 32, 23, 21, 33, 25
* A: TBD

Table: basic mean evaluation

+-----------+-------------------+-----------------------+-----------------------+
| concept   | mean              | median                | mode                  |
+===========+===================+=======================+=======================+
| what?     | arithmetic mean   | sort, middle          | most frequent         |
+-----------+-------------------+-----------------------+-----------------------+
| why?      | eval trend        | eval trend            | eval trend            |
+-----------+-------------------+-----------------------+-----------------------+
| how?      | total / n         | sorted(seq)[int(n/2)] | Hashmap               |
+-----------+-------------------+-----------------------+-----------------------+
| Time      | O(n)              | O(n)                  | O(1)                  |
| complexity|                   |                       |                       |
+-----------+-------------------+-----------------------+-----------------------+
| Space     | O(2)              | O(n)                  | O(c), c <= n          |
| complexity|                   |                       |                       |
+-----------+-------------------+-----------------------+-----------------------+

"""
import sys
sys.path.append('.')
from libraries.pkg.stats import SimpleStatistics
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')

data = [23, 29, 20, 32, 23, 21, 33, 25]
ss = SimpleStatistics(data)
logging.debug('sum      : {}'.format(ss.get_sum()))
logging.debug('mean     : {}'.format(ss.mean()))
logging.debug('median   : {}'.format(ss.median()))
logging.debug('mode     : {}'.format(ss.mode()))
logging.debug('range    : {}'.format(ss._range()))
logging.debug('midrange : {}'.format(ss._midrange()))

data2 = [3, 3, 3, 3, 3, 100]
ss2   = SimpleStatistics(data2)
logging.debug(f'{"-" * 50}')
logging.debug('sum      : {}'.format(ss2.get_sum()))
logging.debug('mean     : {}'.format(ss2.mean()))
logging.debug('median   : {}'.format(ss2.median()))
logging.debug('mode     : {}'.format(ss2.mode()))
logging.debug('range    : {}'.format(ss2._range()))
logging.debug('midrange : {}'.format(ss2._midrange()))
