# The median is the middle number in a sorted sequence of numbers.
# Finding the median of [7,12,3,1,6] would first consist of sorting the sequence into [1,3,6,7,12] and then locating the middle value, which would be 6.
# If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.
# For example, the median of the sequence [7,3,1,4] is 3.5, since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.
# You can sort the sequence using the sorted() function, like so:

def median(myls):
    """ find median of a list """
    nr = len(myls) # list length
    myls = sorted(myls)  # first sort the list
    if  nr %2 != 0: # odd nr of elements
        ind = int(nr/2) # middle of list
        return myls[ind]
    else: # no middle element, take mean of two adjacent
        ind = int(nr/2)-1
        return float( myls[ind] + myls[ind+1])/2.
