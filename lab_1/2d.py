import math
from graphics import *
import time
import numpy as np

xw = 900
yw = 900

st = 80
side = 150  # increasing side length for better visualization
half_side = side / 2
h = math.sqrt(side ** 2 - half_side ** 2)

teta_d = 60
teta = (3 / 14 * teta_d) / 180

Sx = 1.6
Sy = 1.2


def create_win(title):
    win = GraphWin(title, xw, yw)
    win.setBackground('yellow')
    return win


def draw_parallelogram(win, point_a, point_b, point_c, point_d):
    obj = Polygon(point_a, point_b, point_c, point_d)
    obj.draw(win)


def create_start_parallelogram():
    x1 = st
    y1 = yw - st
    x2 = x1 + side
    y2 = y1
    x3 = x2 - half_side
    y3 = y1 - h
    x4 = x1 - half_side
    y4 = y3
    return np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])


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

points = create_start_parallelogram()
x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]
x4, y4 = points[3]

draw_parallelogram(win, Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))

stop = xw / side
stop = float(stop)
ii = int(stop)

for i in range(ii):
    time.sleep(0.3)

    total = move_point(x1, y1)
    x1, y1 = total[0][:2]

    total = move_point(x2, y2)
    x2, y2 = total[0][:2]

    total = move_point(x3, y3)
    x3, y3 = total[0][:2]

    total = move_point(x4, y4)
    x4, y4 = total[0][:2]

    draw_parallelogram(win, Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))

win.getMouse()
win.close()

# Rotating
win = create_win("2-D Rotating")

points = create_start_parallelogram()
x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]
x4, y4 = points[3]

draw_parallelogram(win, Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))

stop = xw / side * 6
stop = float(stop)
ii = int(stop)

for i in range(ii):
    time.sleep(0.3)

    total = move_point(x1, y1)
    total = rotate_point(total[0, 0], total[0, 1])
    x1, y1 = total[0][:2]

    total = move_point(x2, y2)
    total = rotate_point(total[0, 0], total[0, 1])
    x2, y2 = total[0][:2]

    total = move_point(x3, y3)
    total = rotate_point(total[0, 0], total[0, 1])
    x3, y3 = total[0][:2]

    total = move_point(x4, y4)
    total = rotate_point(total[0, 0], total[0, 1])
    x4, y4 = total[0][:2]

    draw_parallelogram(win, Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))

win.getMouse()
win.close()

# Scaling
win = create_win("2-D Scaling")

points = create_start_parallelogram()
x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]
x4, y4 = points[3]

draw_parallelogram(win, Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))

total = move_point(x1, y1, 20)
total = scale_point(total[0, 0], total[0, 1])
x1, y1 = total[0][:2]

total = move_point(x2, y2, 20)
total = scale_point(total[0, 0], total[0, 1])
x2, y2 = total[0][:2]

total = move_point(x3, y3, 20)
total = scale_point(total[0, 0], total[0, 1])
x3, y3 = total[0][:2]

total = move_point(x4, y4, 20)
total = scale_point(total[0, 0], total[0, 1])
x4, y4 = total[0][:2]

draw_parallelogram(win, Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))

win.getMouse()
win.close()
