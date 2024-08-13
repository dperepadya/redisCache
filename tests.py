import time
import unittest

import redis

import main

r_cache = redis.Redis(host='localhost', port=6379, decode_responses=True)


fibo_dict = {
    1: 0,
    2: 1,
    3: 1,
    4: 2,
    5: 3,
    6: 5,
    7: 8,
    8: 13,
    9: 21,
    10: 34
}

class TestFibo(unittest.TestCase):
    def setUp(self):
        r_cache.flushdb()

    def test_fibo(self):
        for n, value in fibo_dict.items():
            self.assertEqual(main.fibo(n), value)

    def test_fibo_wrong_input(self):
        with self.assertRaises(ValueError):
            main.fibo(0)


if __name__ == '__main__':
    unittest.main()
