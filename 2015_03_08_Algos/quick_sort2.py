def quick_sort(array):
    """ quick sort """
    if len(array) > 1:
        pivot_index = len(array) / 2
        pivot_value = array[pivot_index]
        # split array
        smaller = []
        larger = []
        for i in range(len(array)):
            if i != pivot_index:
                if array[i] < pivot_value:
                    smaller.append(array[i])
                else:
                    larger.append(array[i])
        quick_sort(smaller)
        quick_sort(larger)
        array[:] = smaller + [pivot_value] + larger
