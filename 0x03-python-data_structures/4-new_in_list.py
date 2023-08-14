#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lst = []
    for i in range(0, len(my_list)):
        lst.append(my_list[i])
    if isx < 0 or idx >= len(my_list):
        return lst
    else:
        lst[idx] = element
        return lst
