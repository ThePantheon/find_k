#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: yangtian


def sum_of_integers(integers):
    return sum(integers)


def sum_of_integers_exclude_k(integers, start):
    length_exclude_k = len(integers) - 1
    return (length_exclude_k
            * (length_exclude_k + 2*start - 1)
            / 2)


def find_k_use_math(integers, start):
    return (sum_of_integers(integers)
            - sum_of_integers_exclude_k(integers, start))


def is_pointing_inside_list(integers, pointer):
    return (0 < pointer and pointer < len(integers))


def is_positive_number(integers, pointer):
    return (integers[pointer] > 0)


def reverse_pointed_value(integers, pointer):
    integers[pointer] = -integers[pointer]


def find_k_use_loop(integers, start):
    offset = start - 1
    for i in xrange(0, len(integers)):
        pointer = abs(integers[i]) - offset
        if (is_pointing_inside_list(integers, pointer) and
            is_positive_number(integers, pointer)):
            reverse_pointed_value(integers, pointer)
        else:
            return pointer + offset
