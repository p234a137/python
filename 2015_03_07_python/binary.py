
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11


# 2**0 = 1
# 2**1 = 2
# 2**2 = 4
# 2**3 = 8
# 2**4 = 16
# 2**5 = 32
# 2**6 = 64
# 2**7 = 128
# 2**8 = 256
# 2**9 = 512
# 2**10 = 1024

one = 0b1
two = 0b10
three = 0b11
four  = 0b100
five  = 0b101
six  = 0b110
seven  = 0b111
eight = 0b1000
nine = 0b1001
ten  = 0b1010
eleven = 0b1011
twelve = 0b1100


# In [22]: ?oct
# Type:       builtin_function_or_method
# String Form:<built-in function oct>
# Namespace:  Python builtin
# Docstring:
# oct(number) -> string

# Return the octal representation of an integer or long integer.

# In [23]: ?hex
# Type:       builtin_function_or_method
# String Form:<built-in function hex>
# Namespace:  Python builtin
# Docstring:
# hex(number) -> string

# Return the hexadecimal representation of an integer or long integer.

for i in range(1,6):
        print i, bin(i)
# 1 0b1
# 2 0b10
# 3 0b11
# 4 0b100
# 5 0b101


# int()'s Second Parameter
# Python has an int() function that you've seen a bit of already. It can turn non-integer input into an integer, like this:

int("42")
# ==> 42
# What you might not know is that the int function actually has an optional second parameter.

int("110", 2)
# ==> 6
# When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.



print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001",2)



# Slide to the Left! Slide to the Right!
# The next two operations we are going to talk about are the left and right shift bitwise operators. These operators work by shifting the bits of a number over by a designated number of slots.
# The block below shows how these operators work on the bit level. Note that in the diagram, the shift is always a positive integer:
# Left Bit Shift (<<)  
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)       

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0) 

# This operation is mathematically equivalent to floor dividing and multiplying by 2 (respectively) for every time you shift, but it's often easier just to think of it as shifting all the 1s and 0s left or right by the specified number of slots.
# Note that you can only do bitwise operations on an integer. Trying to do them on strings or floats will result in nonsensical output!

shift_right = 0b1100
shift_left = 0b1
# Your code here!
shift_right >> 2
shift_left << 2
print bin(shift_right)
print bin(shift_left)


# A BIT of This AND That
# The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of both numbers are 1. For example:
#      a:   00101010   42
#      b:   00001111   15       
# ===================
#  a & b:   00001010   10
# As you can see, the 2's bit and the 8's bit are the only bits that are on in both a and b, so a & b only contains those bits. Note that using the & operator can only result in a number that is less than or equal to the smaller of the two values.
# So remember, for every given bit in a and b:

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
# Therefore,
 0b111 (7) & 0b1010 (10) = 0b10
# which equals two.

# Instructions
# print out the result of calling bin() on 0b1110 & 0b101.
# See if you can guess what the output will be!
print bin(0b1110 & 0b101)

# A BIT of This OR That
# The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1. For example:
#     a:  00101010  42
#     b:  00001111  15       
# ================
# a | b:  00101111  47
# Note that the bitwise | operator can only create results that are greater than or equal to the larger of the two integer inputs.
# So remember, for every given bit in a and b:
0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1
# Meaning
 110 (6) | 1010 (10) = 1110 (14)

print bin(0b1110 | 0b101)






# This XOR That?
# The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.
#     a:  00101010   42
#     b:  00001111   15       
# ================
# a ^ b:  00100101   37
# Keep in mind that if a bit is off in both numbers, it stays off in the result. Note that XOR-ing a number with itself will always result in 0.
# So remember, for every given bit in a and b:
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
# Therefore:
 111 (7) ^ 1010 (10) = 1101 (13)

print bin(0b1110 ^ 0b101)





# See? This is NOT That Hard!
# The bitwise NOT operator (~) just flips all of the bits in a single number. What this actually means to the computer is actually very complicated, so we're not going to get into it. Just know that mathematically, this is equivalent to adding one to the number and then making it negative.
# And with that, you've seen all of the basic bitwise operators! We'll see what we can do with these in the next section.
print ~1 # -2
print ~2 # -3
print ~3 # -4
print ~42 # -43
print ~123 # -124



# The Man Behind the Bit Mask
# A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
    print "Bit was on"
# In the example above, we want to see if the third bit from the right is on.

# First, we first create a variable num containing the number 12, or 0b1100.
# Next, we create a mask with the third bit on.
# Then, we use a bitwise-and operation to see if the third bit from the right of num is on.
# If desired is greater than zero, then the third bit of num must have been one.
def check_bit4(input):
    mask = 0b1000
    if input & mask > 0:
        return "on"
    else:
        return "off"



# Turn It On
# You can also use masks to turn a bit in a number on using |. For example, let's say I want to make sure the rightmost bit of number a is turned on. I could do this:
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7
# Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.

# In the editor is a variable, a. Use a bitmask and the value a in order to achieve a result where the third bit from the right of a is turned on. Be sure to print your answer as a bin() string!
a = 0b10111011
bitmask = 0b100
print bin(a | bitmask)


# Just Flip Out
# Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped.
# For example, let's say I want to flip all of the bits in a. I might do this:
a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1

# In the editor is the 8 bit variable a. Use a bitmask and the value a in order to achieve a result where all of the bits in a are flipped. Be sure to print your answer as a bin() string!
a     = 0b11101110
mask = 0b11111111
print bin(a^mask)


# Slip and Slide
# Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place.

a = 0b101 
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten 
desired = a ^ mask
# Let's say that I want to turn on the 10th bit from the right of the integer a.
# Instead of writing out the entire number, we slide a bit over using the << operator.
# We use 9 because we only need to slide the mask nine places over from the first bit to reach the tenth bit.

# Define a function called flip_bit that takes the inputs (number, n).
# Flip the nth bit (with the ones bit being the first bit) and store it in result.
# Return the result of calling bin(result).
def flip_bit(number, n):
    mask = 0b1 << (n-1)
    result = number ^ mask
    return bin(result)
