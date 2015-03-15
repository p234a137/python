import random

array = [random.randint(-20, 60) for i in range(32)]

from heap_sort import *

print ' array', array
heap_sort(array)
print 'sorted', array
