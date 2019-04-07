# -*- encoding:utf8 -*-
class p6_1:
    @classmethod
    def hanoi(cls, n, from_pos, to_pos, aux_pos):
        '''
        :param n: 원반갯수 
        :param from_pos: 시작 기둥
        :param to_pos:  도착 기둥
        :param aux_pos: 중간 기둥
        :return: 
        '''
        if n == 1:
            print from_pos, "->", to_pos
            return

        cls.hanoi(n - 1, from_pos, aux_pos, to_pos)
        print from_pos, "->", to_pos
        cls.hanoi(n - 1, aux_pos, to_pos, from_pos)

print "n = 1"
p6_1.hanoi(1, 1, 3, 2)
print '='*30

print "n = 2"
p6_1.hanoi(2, 1, 3, 2)
print '='*30

print "n = 3"
p6_1.hanoi(2, 1, 3, 2)
print '='*30

print "n = 4"
p6_1.hanoi(3, 1, 3, 2)
print '='*30
