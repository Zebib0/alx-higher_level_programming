#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    a0 = tuple_a[0]
    a1 = tuple_a[1]
    b0 = tuple_b[0]
    b1 = tuple_b[1]

    sum = a0 + b0
    sum1 = a1 + b1
    sum_tot = [sum, sum1]
    return (tuple(sum_tot))
