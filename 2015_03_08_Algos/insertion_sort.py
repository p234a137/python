def insertion_sort(items):
    """ insertion sort"""
    for i in range(1,len(items)):
        j=i
        # push as much to the left as possible
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
