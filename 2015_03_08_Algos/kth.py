def kth(sample, k):
    pivot_index = len(sample)/2
    pivot = sample[pivot_index]
    below = [s for s in sample if s < pivot]
    above = [s for s in sample if s > pivot]
    i, j = len(sample) - len(below), len(above)

    if k < j:      return kth(above, k)
    elif k > i:   return kth(below, k-i)
    else:          return pivot


""" test sorting algorithms """
import random
array = [random.randint(-100,100) for i in range(32)]
print ' array', array

k = 19
kth_value = kth(array, k)
print 'k=',k, ' value = ',kth_value

array.sort()
print "sorted", array
print array[len(array)-k]
