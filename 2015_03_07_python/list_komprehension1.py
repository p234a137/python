evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50


doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
print doubles_by_3

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1,12) if x %2 == 0]
print even_squares


cubes_by_four = [x**3 for x in range(1,11) if x**3 %4 == 0]
print cubes_by_four

# Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives = [x for x in range(1,16) if x%3 == 0 or x%5 == 0]
