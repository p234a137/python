def quick_sort(array):
    """ quick sort """
    if len(array) > 1:
        pivot_point = len(array) / 2
        pivot_value = array[pivot_point]
        below = [s for s in array if s < pivot_value]
        above = [s for s in array if s > pivot_value]
        quick_sort(below)
        quick_sort(above)
        array[:] = below + [pivot_value] + above
