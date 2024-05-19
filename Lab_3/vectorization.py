import tkinter
import numpy as np

class Pyramid:
    def __init__(self, canvas, points):
        self.canvas = canvas
        self.points = points
        self.color = "black"
        self.x = 0
        self.y = 0
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

    def set_color(self, face_index, color):
        self.color = color  # Simplified for all faces

    def move(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, angle_x=0, angle_y=0, angle_z=0):
        self.angle_x = angle_x
        self.angle_y = angle_y
        self.angle_z = angle_z

    def draw_using_lagrange_interpolation(self, point_num):
        self.draw()

    def draw_using_lagrange_interpolation_and_z_buffer(self, point_num, colors):
        self.draw()

    def draw(self):
        # Implement basic drawing logic
        for point in self.points:
            x, y = self.project_point(point)
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=self.color)

    def project_point(self, point):
        # Simplified projection ignoring 3D transformations for now
        return self.x + point[0], self.y + point[1]

# Sample points for a basic pyramid
points = np.array([
    # base
    [0, 0, 50, 1],
    [0, 100, 50, 1],
    [100, 100, 50, 1],
    [100, 0, 50, 1],
    [0, 0, 50, 1],

    # triangles
    [50, 50, 200, 1],
    [100, 0, 50, 1],
    [0, 0, 50, 1],

    [50, 50, 200, 1],
    [0, 100, 50, 1],
    [0, 0, 50, 1],

    [50, 50, 200, 1],
    [100, 100, 50, 1],
    [0, 100, 50, 1],

    [50, 50, 200, 1],
    [100, 0, 50, 1],
    [100, 100, 50, 1],

    # return to center
    [0, 100, 50, 1],
    [0, 0, 50, 1],
])

root = tkinter.Tk()
root.title("3D Graphics")
root.geometry("1200x600")
canvas = tkinter.Canvas(root, bg="white", bd=0, border=0, width=1200, height=600, background="white")
canvas.pack()

pyramid1 = Pyramid(canvas, points)
pyramid1.set_color(3, "red")
pyramid1.move(100, 300)
pyramid1.rotate(angle_x=0, angle_y=55, angle_z=90)
pyramid1.draw_using_lagrange_interpolation(point_num=170)

pyramid2 = Pyramid(canvas, points)
pyramid2.set_color(3, "green")
pyramid2.move(250, 300)
pyramid2.rotate(angle_x=0, angle_y=55, angle_z=90)
pyramid2.draw()

root.mainloop()
