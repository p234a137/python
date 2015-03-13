
# censor
# Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.
# For example:
# censor("this hack is wack hack", "hack") 
# should return
# "this **** is wack ****"
# Assume your input strings won't contain punctuation or upper case letters.
# The number of asterisks you put should correspond to the number of letters in the censored word.
def censor(text, word):
    stext = text.split()
    wl = len(word)
    for i in range(len(stext)):
        if stext[i] == word:
            stext[i] = "*" * wl
    print " ".join(stext)
    return " ".join(stext)
