import re


def duplicate_encode(word):
    # your code here

    # takes word and make it .lower and define result string
    word = word.lower()
    rslt_string = ""
    # for loop it
    for char in word:
        if word.count(char) == 1:
            rslt_string += '('
        else:
            rslt_string += ')'

    return rslt_string

    # vomits out what i need it to













