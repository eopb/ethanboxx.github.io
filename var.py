#!/usr/bin/env python2
from __future__ import division
import colorsys
from random import randint


def setupImportant():
    global field_width
    global field_height
    global numberOfSnakes
    global computerAi
    global SnakeHue
    SnakeHue = colorsys.hsv_to_rgb((randint(1, 10000)/10000), (randint(1, 10000)/10000), 1)
    print (str(SnakeHue))
    computerAi = True
    try:
        gridSize = input("What do you want the Grid size to be? I recommend 10.")
        int(gridSize)
        field_width, field_height = gridSize, gridSize
    except:
        print ("Error when using grid size! Grid size has been reset to default.")
        field_width, field_height = 10, 10
    try:
        numberOfSnakes = input("What do you want the number of snakes to be? I recommend 1.")
        int(numberOfSnakes)
    except:
        print ("Error when using number of snakes! Number of snakes has been reset to default.")
        numberOfSnakes = 1
