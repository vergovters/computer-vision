from graphics import *
import numpy as np
import math as mt
import time

xw = 1000
yw = 1000
st = 200

figure = np.array([[0, 0, 0, 1],
                   [st*3, 0, 0, 1],
                   [st*3, st*3, 0, 1],
                   [0, st*3, 0, 1],
                   [0, 0, st * 4, 1],
                   [st*3, 0, st * 4, 1],
                   [st*3, st*3, st * 4, 1],
                   [0, st*3, st * 4, 1]])


def create_win(title):
    win = GraphWin(title, xw, yw)
    win.setBackground('white')
    return win


def move_center(figure):
    m = xw / 3
    f = np.array([[1, 0, 0, m], [0, 1, 0, m], [0, 0, 1, m], [1, 0, 0, 1]])  # translation matrix
    ft = f.T
    Prxy = figure.dot(ft)
    return Prxy


def dimetri(figure, TetaG1, TetaG2):
    TetaR1 = (3 / 14 * TetaG1) / 180
    TetaR2 = (3 / 14 * TetaG2) / 180

    f1 = np.array(
        [[mt.cos(TetaR1), 0, -mt.sin(TetaR1), 0], [0, 1, 0, 0], [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1], [0, 0, 0, 1]])
    ft1 = f1.T
    Prxy1 = figure.dot(ft1)

    f2 = np.array(
        [[1, 0, 0, 0], [0, mt.cos(TetaR2), mt.sin(TetaR2), 0], [0, -mt.sin(TetaR2), mt.cos(TetaR2), 0], [0, 0, 0, 1]])
    ft2 = f2.T
    Prxy2 = Prxy1.dot(ft2)
    return Prxy2


def draw(figure, outlineColor):
    A = Point(figure[0, 0], figure[0, 1])
    B = Point(figure[1, 0], figure[1, 1])
    I = Point(figure[2, 0], figure[2, 1])
    M = Point(figure[3, 0], figure[3, 1])

    D = Point(figure[4, 0], figure[4, 1])
    C = Point(figure[5, 0], figure[5, 1])
    F = Point(figure[6, 0], figure[6, 1])
    E = Point(figure[7, 0], figure[7, 1])

    obj = Polygon(A, B, I, M)
    obj.setOutline(outlineColor)
    obj.draw(win)

    obj = Polygon(D, C, F, E)
    obj.setOutline(outlineColor)
    obj.draw(win)

    obj = Polygon(A, B, C, D)
    obj.setOutline(outlineColor)
    obj.draw(win)

    obj = Polygon(M, I, F, E)
    obj.setOutline(outlineColor)
    obj.draw(win)


win = create_win("3-D")

Figure1 = move_center(figure)
Figure2 = dimetri(Figure1, 180, -90)
draw(Figure2, "black")
time.sleep(1)
draw(Figure2, "gray")
time.sleep(1)
draw(Figure2, "dark gray")
time.sleep(1)
draw(Figure2, "light gray")
time.sleep(1)
draw(Figure2, "white")

win.getMouse()
win.close()