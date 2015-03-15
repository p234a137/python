def insertion_sort(array):
    """ insertion sort """
    for i in range(len(array)):
        j = i
        # push as much to the left as possible
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
