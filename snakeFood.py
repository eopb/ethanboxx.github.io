#!/usr/bin/env python2
from random import randint
import var
def spawnFood(snake):
    #global snake
    global xfood
    global yfood
    global food
    food = [] # food list of type (x, y)

    xfood, yfood = randint(0, (var.field_width-1)), randint(0, (var.field_height-1)) # 
#random spawn pos
    while foodSaftyCheck(snake) == False:
        xfood, yfood = randint(0, (var.field_width-1)), randint(0, (var.field_height-1)) 
# random spawn pos
    food.append((xfood, yfood))
    print ("Food spawned at [" + str(xfood) + "," + str(yfood)+"].")

def foodSaftyCheck(snake):
    for x, y in snake:
            if x == xfood and y == yfood:
                print ("Could not add food at [" +str(xfood)+ "," +str(yfood)+ "] due to a snake being there. Retrying")
                return False
            else:
                pass
    return True
