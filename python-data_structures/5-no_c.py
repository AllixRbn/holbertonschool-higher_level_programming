#!/usr/bin/python3

def no_c(my_string):
    string_with_no_c = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            string_with_no_c += char
    return string_with_no_c
