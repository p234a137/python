import heapq

def heap_sort(array):
    """ heap sort """
    heapq.heapify(array)
    array[:] = [heapq.heappop(array) for i in range(len(array))]
