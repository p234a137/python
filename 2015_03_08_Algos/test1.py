
# http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python
# Each sorting algorithm is implemented as a Python function, which will sort the list in-place. I used the following piece of code to test all the algorithms.

import random
from heap_sort import *

random_items = [random.randint(-50, 100) for c in range(32)]

print 'Before: ', random_items
heap_sort(random_items)
print 'After : ', random_items
