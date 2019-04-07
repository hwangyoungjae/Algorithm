# -*- encoding:utf8 -*-

class p4_1:
    @classmethod
    def fact(cls, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


class p4_2:
    @classmethod
    def fact(cls, n):
        if n <= 1:
            return 1
        return n * cls.fact(n - 1)


class practice:
    @classmethod
    def p4_1(cls, n):
        if n <= 1:
            return 1
        return n + cls.p4_1(n - 1)


print p4_1.fact(1)
print p4_1.fact(5)
print p4_1.fact(10)

print p4_2.fact(1)
print p4_2.fact(5)
print p4_2.fact(10)

print practice.p4_1(100)