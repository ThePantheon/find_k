#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: yangtian


import random
import heapq
import unittest
from find_k import find_k_use_math, find_k_use_loop


def gen_integers(n, m):
    if n < m:
        k = random.randint(n, m)
    elif (1 < m and m < n):
        k = random.randint(1, n)
    else:
        k = m
    integers = range(1, n+1) + [k]
    random.shuffle(integers)
    return integers, k


def print_largest_two_integers_and_k(integers, k):
    two_largest = heapq.nlargest(2, integers)
    print ("Largest, second_largest, and k: %d, %d, %d"
           % (two_largest[0], two_largest[1], k))


class FindKTest(unittest.TestCase):

    def test_k_greater_than_n(self):
        n = 65536 * 10
        m = 65536 * 20
        integers, k = gen_integers(n, m)
        print_largest_two_integers_and_k(integers, k)
        self.assertEqual(find_k_use_math(integers), k)
        self.assertEqual(find_k_use_loop(integers), k)

    def test_k_less_than_or_equal_to_n(self):
        n = 65536 * 10
        m = 65536
        integers, k = gen_integers(n, m)
        print_largest_two_integers_and_k(integers, k)
        self.assertEqual(find_k_use_math(integers), k)
        self.assertEqual(find_k_use_loop(integers), k)

    def test_k_equal_to_1(self):
        n = 65536 * 10
        m = 1
        integers, k = gen_integers(n, m)
        print_largest_two_integers_and_k(integers, k)
        self.assertEqual(find_k_use_math(integers), k)
        self.assertEqual(find_k_use_loop(integers), k)

    def test_k_equal_to_n(self):
        n = 65536 * 10
        m = n
        integers, k = gen_integers(n, m)
        print_largest_two_integers_and_k(integers, k)
        self.assertEqual(find_k_use_math(integers), k)
        self.assertEqual(find_k_use_loop(integers), k)

if __name__ == '__main__':
    unittest.main()
