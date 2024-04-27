from graphics import *
import numpy as np
import math as mt

st = 100
Prlpd = np.array([[0, 0, 0, 1],
                  [st, 0, 0, 1],
                  [st, st, 0, 1],
                  [0, st, 0, 1],
                  [0, 0, st * 2, 1],
                  [st, 0, st * 2, 1],
                  [st, st, st * 2, 1],
                  [0, st, st * 2, 1]])


def shift_xyz(Figure, l, m, n):
    f = np.array([[1, 0, 0, l], [0, 1, 0, m], [0, 0, 1, n], [1, 0, 0, 1]])
    ft = f.T
    Prxy = Figure.dot(ft)

    return Prxy


def insert_x(Figure, TetaG):
    TetaR = (3 / 14 * TetaG) / 180
    f = np.array(
        [[1, 0, 0, 0], [0, mt.cos(TetaR), mt.sin(TetaR), 0], [0, -mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 0, 1]])
    ft = f.T
    Prxy = Figure.dot(ft)

    return Prxy


def dimetri(Figure, TetaG1, TetaG2):
    TetaR1 = (3 / 14 * TetaG1) / 180
    TetaR2 = (3 / 14 * TetaG2) / 180
    f1 = np.array(
        [[mt.cos(TetaR1), 0, -mt.sin(TetaR1), 0], [0, 1, 0, 0], [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1], [0, 0, 0, 0], ])
    ft1 = f1.T
    Prxy1 = Figure.dot(ft1)
    f2 = np.array(
        [[1, 0, 0, 0], [0, mt.cos(TetaR2), mt.sin(TetaR2), 0], [0, -mt.sin(TetaR2), mt.cos(TetaR2), 0], [0, 0, 0, 1]])
    ft2 = f2.T
    Prxy2 = Prxy1.dot(ft2)

    return Prxy2


def create_basic_polynomial(x_values, i):
    def basic_polynomial(x):
        divider = 1
        result = 1
        for j in range(len(x_values)):
            if j != i:
                result *= (x - x_values[j])
                divider *= (x_values[i] - x_values[j])
        return result / divider

    return basic_polynomial


def create_lagrange_polynomial(x_values, y_values):
    basic_polynomials = []
    for i in range(len(x_values)):
        basic_polynomials.append(create_basic_polynomial(x_values, i))

    def lagrange_polynomial(x):
        result = 0
        for i in range(len(y_values)):
            result += y_values[i] * basic_polynomials[i](x)
        return result

    return lagrange_polynomial


def vectorization(x1, y1, x2, y2):
    x_values = brez(x1, y1, x2, y2)[0]
    y_values = brez(x1, y1, x2, y2)[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    x_vectorized = []
    y_vectorized = []

    if dx > dy:
        lag_pol = create_lagrange_polynomial(x_values, y_values)

        for i in range(len(x_values)):
            x_vectorized.append(x_values[i])
            y_vectorized.append(lag_pol(x_values[i]))

            obj = Point(x_values[i], y_values[i])
            obj.setFill('blue')
            obj.draw(win)
    else:
        lag_pol = create_lagrange_polynomial(y_values, x_values)

        for i in range(len(x_values)):
            y_vectorized.append(y_values[i])
            x_vectorized.append(lag_pol(y_values[i]))

            obj = Point(x_values[i], y_values[i])
            obj.setFill('blue')
            obj.draw(win)

    for i in range(len(x_values)):
        obj = Point(x_vectorized[i], y_vectorized[i])
        obj.setFill('red')
        obj.draw(win)

    return vectorization


def brez(x1, y1, x2, y2):
    x_values = []
    y_values = []

    dx = x2 - x1
    dy = y2 - y1
    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
    if dx < 0: dx = -dx
    if dy < 0: dy = -dy
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy
    x, y = x1, y1
    error, t = el / 2, 0

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


def PrlpdWiz_MNK(Prxy3):
    
    Ax1 = Prxy3[0, 0]
    Ay1 = Prxy3[0, 1]
    Bx1 = Prxy3[1, 0]
    By1 = Prxy3[1, 1]
    Ix1 = Prxy3[2, 0]
    Iy1 = Prxy3[2, 1]
    Mx1 = Prxy3[3, 0]
    My1 = Prxy3[3, 1]
    
    Dx1 = Prxy3[4, 0]
    Dy1 = Prxy3[4, 1]
    Cx1 = Prxy3[5, 0]
    Cy1 = Prxy3[5, 1]
    Fx1 = Prxy3[6, 0]
    Fy1 = Prxy3[6, 1]
    Ex1 = Prxy3[7, 0]
    Ey1 = Prxy3[7, 1]

    
    vectorization(Ax1, Ay1, Bx1, By1)
    vectorization(Bx1, By1, Ix1, Iy1)
    vectorization(Ix1, Iy1, Mx1, My1)
    vectorization(Mx1, My1, Ax1, Ay1)
    
    vectorization(Dx1, Dy1, Cx1, Cy1)
    vectorization(Cx1, Cy1, Fx1, Fy1)
    vectorization(Fx1, Fy1, Ex1, Ey1)
    vectorization(Ex1, Ey1, Dx1, Dy1)
    
    vectorization(Ax1, Ay1, Bx1, By1)
    vectorization(Bx1, By1, Cx1, Cy1)
    vectorization(Cx1, Cy1, Dx1, Dy1)
    vectorization(Dx1, Dy1, Ax1, Ay1)
    
    vectorization(Mx1, My1, Ix1, Iy1)
    vectorization(Ix1, Iy1, Fx1, Fy1)
    vectorization(Fx1, Fy1, Ex1, Ey1)
    vectorization(Ex1, Ey1, Mx1, My1)
    
    vectorization(Ax1, Ay1, Mx1, My1)
    vectorization(Mx1, My1, Ex1, Ey1)
    vectorization(Ex1, Ey1, Dx1, Dy1)
    vectorization(Dx1, Dy1, Ax1, Ay1)
    
    vectorization(Bx1, By1, Ix1, Iy1)
    vectorization(Ix1, Iy1, Fx1, Fy1)
    vectorization(Fx1, Fy1, Cx1, Cy1)
    vectorization(Cx1, Cy1, Bx1, By1)
    return PrlpdWiz_MNK


def create_polygon(win, points, fill_color):
    obj = Polygon(*points)
    obj.setFill(fill_color)
    obj.draw(win)


def PrlpdWizReal_G(PrxyDIM, Xmax, Ymax, Zmax):
    Ax = PrxyDIM[0, 0]; Ay = PrxyDIM[0, 1]; Az = PrxyDIM[0, 2]
    Bx = PrxyDIM[1, 0]; By = PrxyDIM[1, 1]; Bz = PrxyDIM[1, 2]
    Ix = PrxyDIM[2, 0]; Iy = PrxyDIM[2, 1]; Iz = PrxyDIM[2, 2]
    Mx = PrxyDIM[3, 0]; My = PrxyDIM[3, 1]; Mz = PrxyDIM[3, 2]

    Dx = PrxyDIM[4, 0]; Dy = PrxyDIM[4, 1]; Dz = PrxyDIM[4, 2]
    Cx = PrxyDIM[5, 0]; Cy = PrxyDIM[5, 1]; Cz = PrxyDIM[5, 2]
    Fx = PrxyDIM[6, 0]; Fy = PrxyDIM[6, 1]; Fz = PrxyDIM[6, 2]
    Ex = PrxyDIM[7, 0]; Ey = PrxyDIM[7, 1]; Ez = PrxyDIM[7, 2]

    FlagF = 1 if (abs(Az - Zmax) > abs(Dz - Zmax)) and (abs(Bz - Zmax) > abs(Cz - Zmax)) \
                 and (abs(Iz - Zmax) > abs(Fz - Zmax)) and (abs(Mz - Zmax) > abs(Ez - Zmax)) else 2

    FlagR = 1 if (abs(Dx - Xmax) > abs(Cx - Xmax)) and (abs(Ax - Xmax) > abs(Bx - Xmax)) \
                 and (abs(Mx - Xmax) > abs(Ix - Xmax)) and (abs(Ex - Xmax) > abs(Fx - Xmax)) else 2

    FlagP = 1 if (abs(Ay - Ymax) > abs(My - Ymax)) and (abs(By - Ymax) > abs(Iy - Ymax)) \
                 and (abs(Cy - Ymax) > abs(Fy - Ymax)) and (abs(Dy - Ymax) > abs(Ey - Ymax)) else 2

    create_polygon(win, [Point(Ex, Ey), Point(Fx, Fy), Point(Ix, Iy), Point(Mx, My)], 'yellow') if FlagP == 2 else None
    create_polygon(win, [Point(Ax, Ay), Point(Bx, By), Point(Cx, Cy), Point(Dx, Dy)], 'yellow') if FlagP == 1 else None
    create_polygon(win, [Point(Bx, By), Point(Ix, Iy), Point(Fx, Fy), Point(Cx, Cy)], 'yellow') if FlagR == 1 else None
    create_polygon(win, [Point(Ax, Ay), Point(Mx, My), Point(Ex, Ey), Point(Dx, Dy)], 'yellow') if FlagR == 2 else None
    create_polygon(win, [Point(Ax, Ay), Point(Bx, By), Point(Ix, Iy), Point(Mx, My)], 'yellow') if FlagF == 2 else None
    create_polygon(win, [Point(Dx, Dy), Point(Cx, Cy), Point(Fx, Fy), Point(Ex, Ey)], 'yellow') if FlagF == 1 else None

    return PrlpdWizReal_G


if __name__ == '__main__':
    
    xw = 600
    yw = 600
    st = 50
    TetaG1 = 160
    TetaG2 = 40
    l = (xw / 2) - st
    m = (yw / 2) - st
    n = m


    win = GraphWin("3-D векторний паралелепіпед проекція на ХУ", xw, yw)
    win.setBackground('white')
    Prlpd1 = shift_xyz(Prlpd, l, m, n)

    
    Prlpd2 = dimetri(Prlpd1, TetaG1, TetaG2)

    
    PrlpdWiz_MNK(Prlpd2)

    PrlpdWizReal_G(Prlpd2, (xw * 2), (yw * 2), (yw * 2))
    win.getMouse()
    win.close()
