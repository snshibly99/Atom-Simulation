from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
atom = None
electron_list = []
click = False


class Electron:
    def __init__(self, e_cx, e_cy, orbit, init_angle):
        self.e_cx = e_cx
        self.e_cy = e_cy
        self.orbit = orbit
        self.init_angle = init_angle
        if orbit == 1:
            self.inc = 2
        elif orbit == 2:
            self.inc = 1.5
        elif orbit == 3:
            self.inc = 1


def electron_center(angle, radius):
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    return x, y


def convert_coordinate(x,y):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    a = x
    b = (WINDOW_HEIGHT) - y 
    return a, b


def circ_point(x, y, cx, cy):
    glVertex2f(x+cx, y+cy)
    glVertex2f(y+cx, x+cy)
    glVertex2f(y+cx, -x+cy)
    glVertex2f(x+cx, -y+cy)
    glVertex2f(-x+cx, -y+cy)
    glVertex2f(-y+cx, -x+cy)
    glVertex2f(-y+cx, x+cy)
    glVertex2f(-x+cx, y+cy)


def mid_circle(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius

    while x < y:
        if d < 0:
            d = d + 2 * x +3
        else:
            d = d + 2 * x - 2 * y + 5
            y -= 1
        x += 1
        circ_point(x, y, cx, cy)


def findZone(x0, y0, x1, y1):
    dy = y1-y0
    dx = x1-x0

    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6


def ZoneZeroConversion(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def zero_to_original_zone(zone, x, y):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, -x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y


def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def MidPointLine(zone, x0, y0, x1, y1):
    dy = y1-y0
    dx = x1-x0
    d_init = 2*dy - dx
    e = 2*dy
    ne = 2*(dy-dx)
    x = x0
    y = y0
    while x <= x1:
        a, b = zero_to_original_zone(zone, x, y)
        draw_points(a, b)
        if d_init <= 0:
            x += 1
            d_init += e
        else:
            x += 1
            y += 1
            d_init += ne


def eight_way_symmetry(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    z0_x0, z0_y0 = ZoneZeroConversion(zone, x0, y0)
    z0_x1, z0_y1 = ZoneZeroConversion(zone, x1, y1)
    MidPointLine(zone, z0_x0, z0_y0, z0_x1, z0_y1)


def initialize():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def Hydrogen():
    glColor3f(255, 255, 255)

    for i in range(690,790):
        eight_way_symmetry(100, i, 100, i)

    for j in range(690, 790):
        eight_way_symmetry(160, j, 160, j)

    for k in range(100, 160):
        eight_way_symmetry(k, 740, k, 740)
            
    eight_way_symmetry(170, 725, 180, 740)

    for l in range(690, 740):
        eight_way_symmetry(180, l, 180, l)

    for m in range(170, 190):
        eight_way_symmetry(m, 690, m, 690)


def Carbon():
    glColor3f(255, 255, 255)

    for i in range(480, 530):
        eight_way_symmetry(i, 790, i, 790)

    eight_way_symmetry(470, 780, 480, 790)

    for j in range(700, 780):
        eight_way_symmetry(470, j, 470, j)
            
    eight_way_symmetry(470, 700, 480, 690)
            
    for k in range(480, 530):
        eight_way_symmetry(k, 690, k, 690)

    for m in range(540, 560):
        eight_way_symmetry(m, 740, m, 740)

    for n in range(690, 740):
        eight_way_symmetry(540, n, 540, n)
         
    for o in range(540, 560):
        eight_way_symmetry(o, 690, o, 690)

    for p in range(690, 710):
        eight_way_symmetry(560, p, 560, p)

    for q in range(540, 560):
        eight_way_symmetry(q, 710, q, 710)

def Phosphorus():
    glColor3f(255, 255, 255)

    for i in range(690, 790):
        eight_way_symmetry(980, i, 980, i)

    for j in range(980, 1020):
        eight_way_symmetry(j, 790, j, 790)
            
    for k in range(980, 1020):
        eight_way_symmetry(k, 745, k, 745)

    for l in range(745, 790):
        eight_way_symmetry(1020, l, 1020, l)

    eight_way_symmetry(1030, 725, 1040, 740)

    for m in range(690, 740):
        eight_way_symmetry(1040, m, 1040, m)

    for n in range(1030, 1050):
        eight_way_symmetry(n, 690, n, 690)

    for o in range(1055, 1075):
        eight_way_symmetry(o, 740, o, 740)

    for p in range(1055, 1075):
        eight_way_symmetry(p, 690, p, 690)

    for q in range(1055, 1075):
        eight_way_symmetry(q, 715, q, 715)

    for r in range(715, 740):
        eight_way_symmetry(1055, r, 1055, r)

    for s in range(690, 715):
        eight_way_symmetry(1075, s, 1075, s)

def show_screen():
    global cx, cy, electron_list, atom

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if atom != None and click == True:
        Hydrogen()
        Carbon()
        Phosphorus()
        
        glColor3f(0.514, 0.055, 0.71)
        glPointSize(2)
        glBegin(GL_POINTS)
        mid_circle(cx, cy, 30)
        glEnd()

        glColor3f(0.514, 0.055, 0.71)
        eight_way_symmetry(cx-20, cy, cx+20, cy)
        eight_way_symmetry(cx, cy+20, cx, cy-20)
        

        if atom == "h":

            glColor3f(0, 232, 255)

            for i in range(691,791):
                eight_way_symmetry(101, i, 101, i)

            for j in range(691, 791):
                eight_way_symmetry(161, j, 161, j)

            for k in range(101, 161):
                eight_way_symmetry(k, 741, k, 741)
            
            eight_way_symmetry(171, 725, 181, 741)

            for l in range(691, 741):
                eight_way_symmetry(181, l, 181, l)

            for m in range(171, 191):
                eight_way_symmetry(m, 691, m, 691)

            glColor3f(1.0, 0.0, 0.0)
            glPointSize(2)
            glBegin(GL_POINTS)
            mid_circle(cx, cy, 100)
            glEnd()
            
        elif atom == "c":

            glColor3f(0, 232, 255)

            for i in range(481, 531):
                eight_way_symmetry(i, 791, i, 791)

            eight_way_symmetry(471, 781, 481, 791)

            for j in range(701, 781):
                eight_way_symmetry(471, j, 471, j)
            
            eight_way_symmetry(471, 701, 481, 691)
            
            for k in range(481, 531):
                eight_way_symmetry(k, 691, k, 691)

            for m in range(541, 561):
                eight_way_symmetry(m, 741, m, 741)

            for n in range(691, 741):
                eight_way_symmetry(541, n, 541, n)
         
            for o in range(541, 561):
                eight_way_symmetry(o, 691, o, 691)

            for p in range(691, 711):
                eight_way_symmetry(561, p, 561, p)

            for q in range(541, 561):
                eight_way_symmetry(q, 711, q, 711)
            

            glColor3f(1.0, 0.0, 0.0)
            glPointSize(2)
            glBegin(GL_POINTS)
            mid_circle(cx, cy, 100)
            glEnd()
            glColor3f(0.0, 1.0, 0.0)
            glPointSize(2)
            glBegin(GL_POINTS)
            mid_circle(cx, cy, 200)
            glEnd()

        elif atom == "p":

            glColor3f(0, 232, 255)

            for i in range(691, 791):
                eight_way_symmetry(981, i, 981, i)

            for j in range(981, 1021):
                eight_way_symmetry(j, 791, j, 791)
            
            for k in range(981, 1021):
                eight_way_symmetry(k, 746, k, 746)

            for l in range(746, 791):
                eight_way_symmetry(1021, l, 1021, l)

            eight_way_symmetry(1031, 726, 1041, 741)

            for m in range(691, 741):
                eight_way_symmetry(1041, m, 1041, m)

            for n in range(1031, 1051):
                eight_way_symmetry(n, 691, n, 691)

            for o in range(1056, 1076):
                eight_way_symmetry(o, 741, o, 741)

            for p in range(1056, 1076):
                eight_way_symmetry(p, 691, p, 691)

            for q in range(1056, 1076):
                eight_way_symmetry(q, 716, q, 716)

            for r in range(716, 741):
                eight_way_symmetry(1056, r, 1056, r)

            for s in range(691, 716):
                eight_way_symmetry(1076, s, 1076, s)
            
            glColor3f(1.0, 0.0, 0.0)
            glPointSize(2)
            glBegin(GL_POINTS)
            mid_circle(cx, cy, 100)
            glEnd()
            glColor3f(0.0, 1.0, 0.0)
            glPointSize(2)
            glBegin(GL_POINTS)
            mid_circle(cx, cy, 200)
            glEnd()
            glColor3f(0.0, 0.0, 1.0)
            glPointSize(2)
            glBegin(GL_POINTS)
            mid_circle(cx, cy, 300)
            glEnd()

        glColor3f(1.0, 1.0, 0)
        glPointSize(2)
        glBegin(GL_POINTS)


        for i in electron_list:
            mid_circle(i.e_cx, i.e_cy, 12)

        glEnd()

        for i in electron_list:
            eight_way_symmetry(i.e_cx-5, i.e_cy, i.e_cx+5, i.e_cy)

    glutSwapBuffers()


def mouseListener(button, state, x, y):
    global cx, cy, electron_list, atom, click
    if atom != None and button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        click = True
        c_X, c_Y = convert_coordinate(x,y)
        cx, cy = c_X, c_Y
        if atom == "h":
            electron_list = [Electron(cx+100, cy, 1, 0)]
        elif atom == "c":
            electron_list = [Electron(cx+100, cy, 1, 0),
                            Electron(cx-100, cy, 1, 180),
                            Electron(cx+200, cy, 2, 0),
                            Electron(cx+200, cy, 2, 90),
                            Electron(cx+200, cy, 2, 180),
                            Electron(cx+200, cy, 2, 270)]
        elif atom == "p":
            electron_list = [Electron(cx+100, cy, 1, 0),
                            Electron(cx-100, cy, 1, 180),
                            Electron(cx+200, cy, 2, 0),
                            Electron(cx+200, cy, 2, 45),
                            Electron(cx+200, cy, 2, 90),
                            Electron(cx+200, cy, 2, 135),
                            Electron(cx+200, cy, 2, 180),
                            Electron(cx+200, cy, 2, 225),
                            Electron(cx+200, cy, 2, 270),
                            Electron(cx+200, cy, 2, 315),
                            Electron(cx+300, cy, 3, 0),
                            Electron(cx+300, cy, 3, 72),
                            Electron(cx+300, cy, 3, 144),
                            Electron(cx+300, cy, 3, 216),
                            Electron(cx+300, cy, 3, 288)]

    glutPostRedisplay()


def keyboardListener(key, x, y):
    global atom, electron_list
    if key == b'h':
        atom = "h"
        electron_list = []
    elif key == b'c':
        atom = "c"
        electron_list = []
    elif key == b'p':
        atom = "p"
        electron_list = []

    glutPostRedisplay()


def animation():
    global electron_list
    for i in electron_list:
        x, y = electron_center(i.init_angle, 100*i.orbit)
        i.e_cx, i.e_cy = x+cx, y+cy
        i.init_angle += i.inc
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Atom Simulation")
glutDisplayFunc(show_screen)
glutIdleFunc(animation)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)
glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()
