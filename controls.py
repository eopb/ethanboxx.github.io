#!/usr/bin/env python2
# Real time keyboard reading.
from __future__ import division
from random import randint
import colorsys
import snakeCalc
import var
def keyboard(*args):
    ESCAPE = '\033'
    #global SnakeHue
    global snake_dir
    snake = snakeCalc.snakes[0]
    x, y = snake[0]
    try:
        x2, y2 = snake[1]
    except:
        x2, y2 = snake[0]
    if var.computerAi:
        pass
    else:
        if args[0] == 'w':
            if len(snake) == 1:
                snakeCalc.snake_dir = (0, 1)
            else:
                if y + 1 != y2:
                    if (y == (var.field_height - 1) and y2 == 0):
                        print ("Snake Cant go there!")
                    else:
                        snakeCalc.snake_dir = (0, 1)                             # up
                else:
                    print ("Snake Cant go there!")
        if args[0] == 's':
            if len(snake) == 1:
                snakeCalc.snake_dir = (0, -1)
            else:
                if (y - 1 != y2):
                    if (y == 0 and y2 == (var.field_height - 1)):
                        print ("Snake Cant go there!")
                    else:
                        snakeCalc.snake_dir = (0, -1)# down
                else:
                    print ("Snake Cant go there!")
        if args[0] == 'a':
            if len(snake) == 1:
                snakeCalc.snake_dir = (-1, 0)
            else:
                if (x - 1 != x2):
                    if (x == 0 and x2 == var.field_width - 1):
                        print ("Snake Cant go there!")
                    else:
                        snakeCalc.snake_dir = (-1, 0)                            # left
                else:
                    print ("Snake Cant go there!")
        if args[0] == 'd':
            if len(snake) == 1:
                snakeCalc.snake_dir = (1, 0)
            else:
                if (x + 1 != x2):
                    if (x == var.field_width - 1 and x2 == 0):
                        print ("Snake Cant go there!")
                    else:
                        snakeCalc.snake_dir = (1, 0)                                   # right
                else:
                    print ("Snake Cant go there!")
    if args[0] == ESCAPE:
        print ("exiting")
        snakeCalc.endGame = True
        #glutDestroyWindow(window)
        #sys.exit()
    if args[0] == 'e':
        var.SnakeHue = colorsys.hsv_to_rgb((randint(1, 10000)/10000), (randint(1, 10000)/10000), 1)
