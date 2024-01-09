#!/usr/bin/python3
def no_c(my_string):
    _len = len(my_string)

    j = 0

    newString = my_string[:]

    for i in range(_len):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            newString = newString[:(i - j)] + my_string[(i + 1):]
            j += 1

    return (newString)
