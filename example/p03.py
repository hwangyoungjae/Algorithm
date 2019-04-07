# -*- encoding:utf8 -*-


class p3_1:
    @classmethod
    def find_same_name(cls, a):
        n = len(a)
        result = set()
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    result.add(a[i])
        return result

    @classmethod
    def find_same_name2(cls, a):
        result = set()
        for idx, a1 in enumerate(a[:-1]):
            for a2 in a[idx + 1:]:
                if a1 == a2:
                    result.add(a1)
        return result

    @classmethod
    def practice(cls, a):
        result = list()
        for name1 in a[:-1]:
            for name2 in a[a.index(name1)+1:]:
                result.append((name1, name2))
        return result


names = ["Tom", "Jerry", "Mike", "Tom"]
print p3_1.find_same_name(names)
print p3_1.find_same_name2(names)

names = ["Tom", "Jerry", "Mike"]
print p3_1.practice(names)
