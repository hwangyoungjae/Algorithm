# -*- encoding:utf8 -*-
import random

class p2_1:
    @classmethod
    def find_max(cls, a):
        n = len(a)
        max_v = a[0]
        for i in range(1, n):
            if a[i] > max_v:
                max_v = a[i]
        return max_v

    @classmethod
    def find_max2(cls, a):
        return max(a)

class p2_2:
    @classmethod
    def find_max(cls, a):
        n = len(a)
        max_idx = 0
        for i in range(1, n):
            if a[i] > a[max_idx]:
                max_idx = i
        return max_idx

    @classmethod
    def find_max2(cls, a):
        max_v = max(a)
        max_idx = a.index(max_v)
        return max_idx


v = [random.randint(1, 10000000) for _ in range(10000)]
print p2_1.find_max(v)
print p2_1.find_max2(v)

v = [random.randint(1, 10000000) for _ in range(10000)]
print p2_1.find_max(v)
print p2_1.find_max2(v)
