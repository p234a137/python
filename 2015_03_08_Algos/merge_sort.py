def merge_sort(array):
    """ merge sort """
    if len(array) > 1:
        mid = len(array)/2
        left = array[0:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        # merge
        l, r = 0, 0
        for i in range(len(array)):
#            if (l < len(left)):
#                lval = left[l]
#            else:
#                l = None
#            if(r < len(right)):
#                rval = right[r]
#            else:
#                r = None
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if  ( (lval is not None) and (rval is not None) and lval < rval) or rval is None:
                array[i] = lval 
                l += 1
            elif( (lval is not None) and (rval is not None) and lval >= rval) or lval is None:
                array[i] = rval 
                r += 1
            else:
                print l, r, i
                print left
                print right
                print array
                raise Exception('Could not merge')
