def anti_vowel(text):
    nl = len(text)
    newstring = ""
    the_vowel = ["a","e","i","o","u"]
    for i in range(nl):
        c = text[i]
        if not (c in the_vowel or c.lower() in the_vowel):
            newstring += c
    print newstring
    return newstring
