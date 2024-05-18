from graphics import *
import numpy as np
import math as mt
import time

xw = 900
yw = 800
st = 30


base_vertices = np.array([[0, 0, 0, 1],
                          [st*15, 0, 0, 1],  
                          [st*6, st, 0, 1]])  
apex = np.array([[st*2, st, st * 0,3, 1]])  

def create_win(title):
    win = GraphWin(title, xw, yw)
    win.setBackground('white')
    return win

def move_center(vertices):
    m = xw / 3
    f = np.array([[1, 0, 0, m], [0, 1, 0, m], [0, 0, 1, m], [0, 0, 0, 1]])  
    ft = f.T
    translated_vertices = vertices.dot(ft)
    return translated_vertices

def draw_pyramid(base_vertices, apex, outlineColor):
    base_points = [Point(vertex[0], vertex[1]) for vertex in base_vertices]
    apex_point = Point(apex[0][0], apex[0][1])

    
    base_triangle = Polygon(*base_points)
    
    base_triangle.setOutline(outlineColor)
    base_triangle.draw(win)

    
    for i in range(len(base_vertices)):
        face = Polygon(base_points[i], base_points[(i+1) % len(base_vertices)], apex_point)
        face.setOutline(outlineColor)
        face.draw(win)

win = create_win("3-D")

base_vertices_centered = move_center(base_vertices)


draw_pyramid(base_vertices_centered, apex, "black")
time.sleep(2)
draw_pyramid(base_vertices_centered, apex, "gray")
time.sleep(2)
draw_pyramid(base_vertices_centered, apex, "red")
time.sleep(2)
draw_pyramid(base_vertices_centered, apex, "blue")
time.sleep(2)
draw_pyramid(base_vertices_centered, apex, "white")

win.getMouse()
win.close()
