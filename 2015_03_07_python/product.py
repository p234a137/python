
def product(seq):
    """ takes a list of integers as input and returns the product of all of the elements in the list."""
    prod = 1.
    for i in seq:
        prod = prod * i
    print int(prod)
    return int(prod)

if __name__=='__main__':      # is file being called from prompt?
    print product([1,2,3,4])
