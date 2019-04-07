# -*- encoding:utf8 -*-


class p1_1:
    @classmethod
    def sum_n(cls, n):
        s = 0
        for i in range(1, n + 1):
            s += i
        return s


class p1_2:
    @classmethod
    def sum_n(cls, n):
        return n * (n + 1) // 2


print p1_1.sum_n(100)
print p1_2.sum_n(100)
