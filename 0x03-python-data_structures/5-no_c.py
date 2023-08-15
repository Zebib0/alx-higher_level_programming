#!/usr/bin/python3
def no_c(my_string):
	c = my_string.count('c')
        stri = list(stri)
        while c:
            stri.remove('c')
            c -= 1
        c = stri.count('C')
        while c:
            stri.remove('C')
            c -= 1
        stri = ''.join(stri)
        return stri
