#!/usr/bin/python3

def safe_print_integer(value):
            var = False
            try:
                print("{:d}".format(value))
                var = True
            except:
                var = False
            return (var)
