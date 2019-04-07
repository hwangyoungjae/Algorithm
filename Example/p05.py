# -*- encoding:utf8 -*-
import unittest


def divisor(n):
    r = list()
    for i in range(1, n+1):
        if n % i == 0:
            r.append(i)
    return r

print divisor(27)




exit(0)

class p5_1:
    @classmethod
    def gcd(cls, a, b):
        i = min(a, b)
        while True:
            if a % i == 0 and b % i == 0:
                return i
            i = i - 1

    @classmethod
    def gcd2(cls, x, y):
        min_v = min(x, y)
        rng_v = range(1, min_v + 1)
        rng_v.reverse()
        for i in rng_v:
            if x % i == 0 and y % i == 0:
                return i


class p5_2:
    @classmethod
    def gcd(cls, x, y):
        if y == 0:
            return x
        return cls.gcd(y, x % y)


class Test(unittest.TestCase):
    def test_p5_1(self):
        self.assertEqual(p5_1.gcd(1, 5), 1)
        self.assertEqual(p5_1.gcd(3, 6), 3)
        self.assertEqual(p5_1.gcd(60, 24), 12)
        self.assertEqual(p5_1.gcd(81, 27), 27)

        self.assertEqual(p5_1.gcd2(1, 5), 1)
        self.assertEqual(p5_1.gcd2(3, 6), 3)
        self.assertEqual(p5_1.gcd2(60, 24), 12)
        self.assertEqual(p5_1.gcd2(81, 27), 27)

    def test_p5_2(self):
        self.assertEqual(p5_2.gcd(1, 5), 1)
        self.assertEqual(p5_2.gcd(3, 6), 3)
        self.assertEqual(p5_2.gcd(60, 24), 12)
        self.assertEqual(p5_2.gcd(81, 27), 27)


unittest.main()
