#!/usr/bin/env python2

# Really cool python snake game!
# Made by Ethan Brierley

from __future__ import division # Lets / be used.

print ("Loading.")

from OpenGL.GL import * # OpenGL Imports.
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLU import gluNewQuadric, gluDisk, gluPartialDisk
from random import randint
import time
import colorsys
import os

# Import files needed

import snakeCalc
import var
import controls
import snakeFood

# Sets up varibles used by this file only

try:
    interval = input("What do you want the speed to be? I recommend 200.") # update interval in milliseconds
    int(interval)
except:
    print ("Error when using interval! Interval has been reset to default.")
    interval = 200
try:
    width = input("What do you want the window width to be? I recommend 500.")
    int(width)
except:
    print ("Error when using width! Width has been reset to default.")
    width = 500
try:
    height = input("What do you want the window height to be? I recommend 500.")
    int(height)
except:
    print ("Error when using height! Height has been reset to default.")
    height = 500
    

var.setupImportant() #Sets up other varibles
snakeCalc.spawnSnakes() #Spawns snakes into the map.

aiToSetUp = True

window = 0                                             # glut window number
snake = snakeCalc.snakes[0]



spawnUntill = True
xprotect = 10000000
yprotect = 10000000


hueSetTime = time.time()

startTime = time.time()

frameRatefps = 0
snakeFood.spawnFood(snakeCalc.snakes[0])


def keyboard(*args):
    controls.keyboard(*args)


def update(value):
    snakeCalc.repeatScript()
    glutTimerFunc(interval, update, 0) # trigger next update

def draw_food():
    glColor3f(0.5, 0.5, 1.0)  # set color to blue
    for x, y in snakeFood.food:         # go through each (x, y) entry
        draw_rect(x, y, 1, 1) # draw it at (x, y) with width=1 and height=1



def glut_print( x,  y,  font, r,  g , b , a):
    printmessage2 = snakeCalc.printmessage + " And the FPS is " + str(int(frameRatefps))
    blending = False 
    if glIsEnabled(GL_BLEND) :
        blending = True

    #glEnable(GL_BLEND)
    glColor3f(r,g,b)
    glRasterPos2f(x,y)
    glTranslatef(x, y, 0)
    for ch in printmessage2 :
        glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) )

    if not blending :
        glDisable(GL_BLEND)
    glTranslatef(0-x, 0-y, 0)
    

def draw_snake():
    global SnakeHue
    snakeInQusetion = 0
    for snake in snakeCalc.snakes:
        snakeInQusetion = snakeInQusetion + 1
        thisSnakeHue = colorsys.rgb_to_hsv(var.SnakeHue[0], var.SnakeHue[1], var.SnakeHue[2])
        hueChange = 1.0/len(snakeCalc.snakes)
        if thisSnakeHue[0] + hueChange*snakeInQusetion > 1:
            SnakeHue = colorsys.hsv_to_rgb(thisSnakeHue[0] + hueChange - 1 ,thisSnakeHue[1], thisSnakeHue[2])
        numberOfTests = 0
        for x, y in snake:# go through each (x, y) entry
            numberOfTests = numberOfTests + 1
            lengthOfSnake = int(len(snake))
            Graying = lengthOfSnake + 2
            Graying = 1/Graying
            Graying = Graying*numberOfTests
            Graying = 1 - Graying
            glColor3f((var.SnakeHue[0]*Graying), (var.SnakeHue[1]*Graying), (var.SnakeHue[2]*Graying))
            #drawCircle(x, y, 0.5, 0)
            draw_rect(x, y, 1, 1) # draw it at (x, y) with width=1 and height=1



def refresh2d_custom(width, height, internal_width, internal_height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, internal_width, 0.0, internal_height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle
    
def drawBoarder():
    glBegin(GL_LINES)
    glVertex2d(var.field_height-1, 2)
    glVertex2d(var.field_width-1, var.field_height-1)
    glVertex2d(2,var.field_width-1)
    glEnd()
   
def drawCircle(x, y, radius, linewidth):
    #glBegin(GL_LINE_LOOP)
    '''Draw a simple circle
 
    :Parameters:
        `pos`: tuple, default to (0, 0)
            Position of circle
        `radius`: float, default to 1.0
            Radius of circle
    '''
    #x, y = pos[0], pos[1]
    with gx_matrix:
        glTranslatef(x, y, 0)
        glScalef(radius, radius, 1.0)
        if linewidth > 0:
            gluDisk(gluNewQuadric(), 1-linewidth/float(radius), 1, 32,1)
        else:
            gluDisk(gluNewQuadric(), 0, 1, 32,1)
    #glEnd()
    #glTranslatef(0-x, 0-y, 0)
    #glScalef(-radius, -radius, -1)
    #glScalef(0,0,0)

def draw():# draw is called all the time
    drawStart = time.time()
    global frameRatefps
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d_custom(width, height, var.field_width, var.field_height)
    #drawCircle()
    draw_food()# draw the food
    #drawCircle(5, 5, 1, 0.2)
    #drawBoarder()
    draw_snake()
    #drawCircle()
    glut_print( 1 , 1 , GLUT_BITMAP_9_BY_15 , 1.0 , 0 , 0 , 1.0 )
    # TODO draw things
    
    glutSwapBuffers()                                  # important for double buffering
    if snakeCalc.endGame:
        print "Game OVER"
        time.sleep(2)
        glutDestroyWindow(window)
        sys.exit()
    else:
        pass
    #print ("The fps is"+str(1.0/(time.time()-drawStart)))
    frameRatefps = 1.0/(time.time()-drawStart)


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)       # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("A Game of snakes")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutTimerFunc(interval, update, 0)                     # trigger next update
glutKeyboardFunc(keyboard)                             # tell opengl that we want to check keys
glutMainLoop()                          # start everything
