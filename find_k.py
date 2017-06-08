#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: yangtian


def sum_of_integers(integers):
    return sum(integers)


def sum_of_integers_exclude_k(integers):
    length_exclude_k = len(integers) - 1
    return (length_exclude_k
            * (length_exclude_k + 1)
            / 2)


def find_k_use_math(integers):
    return (sum_of_integers(integers)
            - sum_of_integers_exclude_k(integers))


def find_index_of_positive_value_from_2nd(integers):
    for i in xrange(1, len(integers)):
        if integers[i] > 0:
            return i
    print "Not found k. Return -1."
    return -1


def find_k_use_loop(integers):
    for i in xrange(0, len(integers)):
        if abs(integers[i]) >= len(integers):
            k = abs(integers[i])
            return k
        else:
            integers[abs(integers[i])] = -integers[abs(integers[i])]
    k = find_index_of_positive_value_from_2nd(integers)
    return k
