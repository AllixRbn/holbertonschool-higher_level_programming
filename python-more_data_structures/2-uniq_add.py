#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    new_list = []
    set_list = set(my_list)
    for i in set_list:
        new_list.append(int(i))
    for j in new_list:
        result += j
    return result
