# -*- encoding:utf8 -*-
import turtle
import random
t = turtle.Pen()
t.speed(0)

distance = 700
square = 70
t.forward(distance/2)
t.backward(distance/2)
t.left(90)
t.forward(distance/2)
t.backward(distance/2)
t.left(90)
t.forward(distance/2)
t.backward(distance/2)
t.left(90)
t.forward(distance/2)
t.backward(distance/2)
t.left(90)
t.forward(distance/2)
t.left(90)
t.forward(distance/2)
t.left(90)
t.forward(distance)
t.left(90)
t.forward(distance)
t.left(90)
t.forward(distance)
t.left(90)
t.forward(distance)
t.left(90)
t.forward(square)

t.left(90)
t.forward(distance)






# t.hideturtle()
turtle.done()

# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# t = turtle.Pen()
# t.speed(0)
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x/100+1)
#     t.forward(x)
#     t.left(59)
# t.hideturtle()
# turtle.done()

# def spiral(sp_len):
#     if sp_len <= 5:
#         return
#     t.forward(sp_len)
#     t.right(90)
#     spiral(sp_len - 5)
#
# t.speed(0)
# spiral(200)
# # t.hideturtle()
# t.done()

# def tree(br_len):
#     if br_len <= 5:
#         return
#     new_len = br_len * 0.7
#     t.forward(br_len)
#     t.right(20)
#     tree(new_len)
#     t.left(40)
#     tree(new_len)
#     t.right(20)
#     t.backward(br_len)
#
#
# t.speed(0)
# t.left(90)
# tree(70)
# t.hideturtle()
# t.done()
