def purify(seq):
    """ removes all odd numbers from a list """
    new_seq = []
    for i in seq:
        if i%2 == 0:
            new_seq.append(i)
    print new_seq
    return new_seq
