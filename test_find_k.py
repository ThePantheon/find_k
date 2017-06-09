#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: yangtian


import random
import unittest
from find_k import find_k_use_math, find_k_use_loop


def gen_integers(start, end, k):
    integers = range(start, end) + [k]
    random.shuffle(integers)
    return integers


class FindKTest(unittest.TestCase):

    def test_k_less_than_start(self):
        n = 65536 * 10
        start = 1024
        end = n + start - 1
        k = random.randint(1, start-1)
        integers = gen_integers(start, end, k)
        self.assertEqual(find_k_use_math(integers, start), k)
        self.assertEqual(find_k_use_loop(integers, start), k)

    def test_k_equal_to_start(self):
        n = 65536 * 10
        start = 1024
        end = n + start - 1
        k = start
        integers = gen_integers(start, end, k)
        self.assertEqual(find_k_use_math(integers, start), k)
        self.assertEqual(find_k_use_loop(integers, start), k)

    def test_k_ge_start_and_le_end(self):
        n = 65536 * 10
        start = 1024
        end = n + start - 1
        k = random.randint(start, end)
        integers = gen_integers(start, end, k)
        self.assertEqual(find_k_use_math(integers, start), k)
        self.assertEqual(find_k_use_loop(integers, start), k)

    def test_k_equal_to_end(self):
        n = 65536 * 10
        start = 1024
        end = n + start - 1
        k = end
        integers = gen_integers(start, end, k)
        self.assertEqual(find_k_use_math(integers, start), k)
        self.assertEqual(find_k_use_loop(integers, start), k)

    def test_k_greater_than_end(self):
        n = 65536 * 10
        start = 1024
        end = n + start - 1
        k = random.randint(end+1, end+n)
        integers = gen_integers(start, end, k)
        self.assertEqual(find_k_use_math(integers, start), k)
        self.assertEqual(find_k_use_loop(integers, start), k)


if __name__ == '__main__':
    unittest.main()
