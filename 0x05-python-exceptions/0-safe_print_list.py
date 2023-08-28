#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    size = 0;
    for i in range(x):
        try:
            print(f"{mylist[i]}", end="")
            size += 1
        except IndexError:
            break
    print("")
    return (size)
