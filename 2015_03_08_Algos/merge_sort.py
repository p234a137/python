def merge_sort(items):
    """ merge sort """
    if len(items) > 1:
        mid = len(items)/2 # determine midpoint, this will be an integer
        left = items[0:mid]
        right = items[mid:]
        merge_sort(left) # recursive lower half
        merge_sort(right) # recursive upper half

        l, r = 0, 0
        for i in range(len(items)): # merge left and right
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if (lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                items[i] = rval
                r += 1
            else:
                raise Exception('Could not merge')
