def reverse(text):
    nl = len(text)
    newstring = ""
    for i in range(nl):
        #print text[nl-i-1],
        newstring += text[nl-i-1]
    print newstring
    return newstring
