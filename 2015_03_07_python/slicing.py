l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]

my_list = range(1, 11) # List of numbers 1 - 10
# print all odd elements. default start index = 0, default end index = last, default stride = 1
print my_list[::2]


# negative stride processes left-to-right
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]

my_list = range(1, 11)
# Create a variable called backwards and set it equal to the reversed version of my_list.
backwards = my_list[::-1]


to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens


to_21 = [i for i in range(1,22)]
odds = to_21[::2]
middle_third = to_21[7:14]

str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
str[start:end:stride]
# You can think of a Python string as a list of characters.

# The string in the editor is garbled in two ways:
# First, our message is backwards;
# Second, the letter we want is every other letter.
# Use list slicing to extract the message and save it to a variable called message
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]


