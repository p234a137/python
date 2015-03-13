def digit_sum(n):
    """ add digits of a positive integer """
    sum = 0
    # convert to string then back
    nstr = str(n)
    for i in range(len(nstr)):
        sum += int(nstr[i])
    return sum

# If you're looking for a challenge, try this: to get the rightmost digit of a number, you can modulo (%) the number by 10. To remove the rightmost digit you can floor divide (//) the number by 10. (Don't worry if you're not familiar with floor division—you can look up the documentation here. Remember, this is a challenge!)
# Try working this into a pattern to isolate all of the digits and add them to a total.
