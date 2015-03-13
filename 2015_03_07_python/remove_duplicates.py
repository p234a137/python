def remove_duplicates(myls):
    """ remove duplicates from list """
    newls = []
    for i in myls:
        if  not (i in newls):
            newls.append(i)
    return newls
