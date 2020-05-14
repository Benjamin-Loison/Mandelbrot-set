z_0 = 0

# z_{n+1} = (z_n)² + c

# |z_n| > 2 => lim_{n->Infinity} |z_n| = +Infinity

from tkinter import *
from math import cos, sin, pi
from numpy import linspace

WINDOW_WIDTH, WINDOW_HEIGHT = 3940, 2160
BLACK = "#000000"
C = 0
MAX_ITERATION = 40

def rgb(rgb):
    return "#%02x%02x%02x" % rgb

def dot(x, y, color = BLACK):
    global canvas
    canvas.create_line(x + 1, y + 1, x + 2, y + 2, fill = color)

tkengine = Tk()
window = Frame(tkengine)
window.pack()
canvas = Canvas(window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg = "#FFFFFF")
canvas.pack()

"""r, theta"""
def draw(x, y):
    global C
    """x = r * cos(theta)
    y = r * sin(theta)
    z = complex(x, y)"""
    z = complex(x, y)
    for i in range(MAX_ITERATION):
        if abs(z) > 2:
            #print(i)
            break
        #z = z ** 2 + C
        z = complex(x ** 2 - y ** 2, y * 2 * x)
    #print(z)
    #dot(x, y, rgb((i, i, 255)))
    if i == MAX_ITERATION:
        dot(x, y, rgb((0, 0, 0)))
    #else:
    #    dot(x, y, rgb((255, 255, 255)))

"""i = 0

for theta in linspace(pi / 360, 2 * pi, 360):
    for r in linspace(0.1, 2, 20):
        #print(r, theta)
        i += 1
        draw(r, theta)"""

"""for w in linspace(-2, 2, 201):
    for h in linspace(-2, 2, 201):
        draw(w, h)
        i += 1

print(i)"""

XMIN, XMAX, YMIN, YMAX = -2, +0.5, -1.25, +1.25
XMAX_MINUS_XMIN_DIVIDED_BY_WINDOW_WIDTH = (XMAX - XMIN) / WINDOW_WIDTH
YMAX_MINUS_YMIN_DIVIDED_BY_WINDOW_HEIGHT = (YMIN - YMAX) / WINDOW_HEIGHT

for y in range(WINDOW_HEIGHT):
    print(y)
    for x in range(WINDOW_WIDTH):
        cx = x * XMAX_MINUS_XMIN_DIVIDED_BY_WINDOW_WIDTH + XMIN
        cy = y * YMAX_MINUS_YMIN_DIVIDED_BY_WINDOW_HEIGHT + YMAX
        xn, yn, n = 0, 0, 0
        while xn * xn + yn * yn < 4 and n < MAX_ITERATION:
            tmp_x = xn
            xn = tmp_x ** 2 - yn ** 2 + cx
            yn = 2 * tmp_x * yn + cy
            n += 1
        if n == MAX_ITERATION:
            dot(x, y, rgb((n, 0, 0)))
        else:
            dot(x, y, rgb((255, 255, 255)))

tkengine.mainloop()