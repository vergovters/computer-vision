import math

from graphics import *
import time
import numpy as np

xw = 900
yw = 900

st = 80
side = 100
half_side = side / 2
h = math.sqrt(side ** 2 - half_side ** 2)

teta_d = 60
teta = (3 / 14 * teta_d) / 180

Sx = 1.6
Sy = 1.2


def create_win(title):
    win = GraphWin(title, xw, yw)
    win.setBackground('blue')
    return win

def draw_triangle(win, point_a, point_b, point_c):
    obj = Polygon(point_a, point_b, point_c)
    obj.draw(win)

def create_start_triangle():
    x1 = st
    y1 = yw - st
    x2 = x1 + half_side
    y2 = y1 - h
    x3 = x1 + side
    y3 = y1
    return np.array([[x1, y1], [x2, y2], [x3, y3]])

def move_point(x, y, plus=0):
    a = np.array([[x, y, 1]])
    f = np.array([[1, 0, half_side + plus], [0, 1, -h - plus], [0, 0, 1]])
    ft = f.T
    total = np.dot(a, ft)
    return total

def rotate_point(x, y):
    a = np.array([[x, y, 1]])
    f = np.array([[math.cos(teta), -math.sin(teta), 0], [math.sin(teta), math.cos(teta), 0], [0, 0, 1]])
    ft = f.T
    total = np.dot(a, ft)
    return total

def scale_point(x, y):
    a = np.array([[x, y, 1]])
    f = np.array([[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]])
    ft = f.T
    total = np.dot(a, ft)
    return total

# Moving
win = create_win("2-D Moving")

poit = create_start_triangle()
x1 = poit[0, 0]
y1 = poit[0, 1]
x2 = poit[1, 0]
y2 = poit[1, 1]
x3 = poit[2, 0]
y3 = poit[2, 1]
draw_triangle(win, Point(x1, y1), Point(x2, y2), Point(x3, y3))

stop = xw / side
stop = float(stop)
ii = int(stop)

for i in range(ii):
    time.sleep(0.3)

    total = move_point(x1, y1)
    x1 = total[0, 0]
    y1 = total[0, 1]

    total = move_point(x2, y2)
    x2 = total[0, 0]
    y2 = total[0, 1]

    total = move_point(x3, y3)
    x3 = total[0, 0]
    y3 = total[0, 1]

    draw_triangle(win, Point(x1, y1), Point(x2, y2), Point(x3, y3))

win.getMouse()
win.close()

# Rotating
win = create_win("2-D Rotating")

poit = create_start_triangle()
x1 = poit[0, 0]
y1 = poit[0, 1]
x2 = poit[1, 0]
y2 = poit[1, 1]
x3 = poit[2, 0]
y3 = poit[2, 1]

draw_triangle(win, Point(x1, y1), Point(x2, y2), Point(x3, y3))

stop = xw / side * 6
stop = float(stop)
ii = int(stop)

for i in range(ii):
    time.sleep(0.3)

    total = move_point(x1, y1)
    total = rotate_point(total[0, 0], total[0, 1])
    x1 = total[0, 0]
    y1 = total[0, 1]

    total = move_point(x2, y2)
    total = rotate_point(total[0, 0], total[0, 1])
    x2 = total[0, 0]
    y2 = total[0, 1]

    total = move_point(x3, y3)
    total = rotate_point(total[0, 0], total[0, 1])
    x3 = total[0, 0]
    y3 = total[0, 1]

    draw_triangle(win, Point(x1, y1), Point(x2, y2), Point(x3, y3))

win.getMouse()
win.close()

# Scaling
win = create_win("2-D Scaling")

poit = create_start_triangle()
x1, y1 = poit[0]
x2, y2 = poit[1]
x3, y3 = poit[2]

draw_triangle(win, Point(x1, y1), Point(x2, y2), Point(x3, y3))

total = move_point(x1, y1, 20)
total = scale_point(total[0, 0], total[0, 1])
x1, y1 = total[0][:2]

total = move_point(x2, y2, 20)
total = scale_point(total[0, 0], total[0, 1])
x2, y2 = total[0][:2]

total = move_point(x3, y3, 20)
total = scale_point(total[0, 0], total[0, 1])
x3, y3 = total[0][:2]

draw_triangle(win, Point(x1, y1), Point(x2, y2), Point(x3, y3))

win.getMouse()
win.close()