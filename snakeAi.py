#!/usr/bin/env python2
import snakeFood
import var

def computerAiMovement2(snake):
    global canIGoUp
    global canIGoDown
    global canIGoRight
    global canIGoLeft
    global snake_dir
    canIGoUp = 3
    canIGoDown = 3
    canIGoRight = 3
    canIGoLeft = 3
    whatDirectionIsImpossible(snake)
    doesItCrash(snake)
    isDeadEnd(snake)
    howDoIGetToFood(snake)
    print ("up "+str(canIGoUp))
    print ("down "+str(canIGoDown))
    print ("left "+str(canIGoLeft))
    print ("right "+str(canIGoRight))
    if canIGoUp >= canIGoLeft and canIGoUp >= canIGoDown and canIGoUp >= canIGoRight:
        snake_dir = (0, 1)
    elif canIGoDown >= canIGoLeft and canIGoDown >= canIGoRight and canIGoDown >= canIGoUp:
        snake_dir = (0, -1)
    elif canIGoLeft >= canIGoDown and canIGoLeft >= canIGoRight and canIGoLeft >= canIGoUp:
        snake_dir = (-1, 0)
    elif canIGoRight >= canIGoDown and canIGoRight >= canIGoLeft and canIGoRight >= canIGoUp:
        snake_dir = (1, 0)
    else:
        print "error"
    return snake_dir


def whatDirectionIsImpossible(snake):
    global canIGoUp
    global canIGoDown
    global canIGoRight
    global canIGoLeft
    possibleDirections = [(0,1),(0,-1),(1,0),(-1,0)]
    x1, y1 = snake[0]
    try:
        x2, y2 = snake[1]
    except:
        x2, y2 = snake[0]
    for x, y in possibleDirections:
        if len(snake) == 1:
            return True
        else:
            if (y + y1 == y2) and (x + x1 == x2):
                if x == -1 or (x1 == 0 and x2 == var.field_width - 1):
                    canIGoLeft = 0
                    print ("cant go dir is left")
                elif x == 1 or (x1 == var.field_width - 1 and x2 == 0):
                    canIGoRight = 0
                    print ("cant go dir is right")
                elif y == 1 or (y1 == (var.field_height - 1) and y2 == 0):
                    print ("cant go dir is up")
                    canIGoUp = 0
                elif y == -1 or (y1 == 0 and y2 == (var.field_height - 1)):
                    print ("cant go dir is down")
                    canIGoDown = 0
                else:
                    print ("This is not possible There must be an error in the code!")
            pass

def doesItCrash(snake):
    global canIGoUp
    global canIGoDown
    global canIGoRight
    global canIGoLeft
    possibleDirections = [(0,1),(0,-1),(1,0),(-1,0)]
    x1, y1 = snake[0]
    try:
        x2, y2 = snake[1]
    except:
        x2, y2 = snake[0]
    (headx, heady) = snake[0]# get the snake's head x and y position
    headlessTaillessSnake = snake[:] #Copy list
    del headlessTaillessSnake[0]
    if len(snake) == 1:
        pass
    else:
        pass
        del headlessTaillessSnake[(len(headlessTaillessSnake))-1]
    for x, y in possibleDirections:
        for bodyx, bodyy in headlessTaillessSnake:
            if len(snake) == 0:
                return True
            else:
                if x1 + x == bodyx and y1 + y == bodyy:
                    if x == -1:
                        if canIGoLeft == 0:
                            canIGoLeft = 0
                        else:
                            canIGoLeft = 1
                    elif x == 1:
                        if canIGoRight == 0:
                            canIGoRight = 0
                        else:
                            canIGoRight = 1
                    elif y == 1:
                        if canIGoUp == 0:
                            canIGoUp = 0
                        else:
                            canIGoUp = 1
                    elif y == -1:
                        if canIGoDown == 0:
                            canIGoDown = 0
                        else:
                            canIGoDown = 1
                    else:
                        pass

                        
                else: pass
                if y == 0 and x == -1 and x1 == 0 and var.field_width - 1 == bodyx and y1 == bodyy and canIGoLeft != 0:
                    canIGoLeft = 1
                    print "got hear 1"
                    #endGame = True
                else: pass
                if y == 0 and x == 1 and x1 == var.field_width - 1 and bodyx == 0 and y1 == bodyy and canIGoRight != 0:
                    canIGoRight = 1
                    print "got hear 2"
                    #endGame = True
                else: pass
                if y == -1 and x == 0 and y1 == 0 and var.field_height - 1 == bodyy and x1 == bodyx and canIGoDown != 0:
                    canIGoDown = 1
                    print "got hear 3"
                    #endGame = True
                else: pass
                if y == 1 and x == 0 and y1 == var.field_height - 1 and bodyy == 0 and x1 == bodyx and canIGoUp != 0:
                    print "got hear 4"
                    #endGame = True
                    canIGoUp = 1
                else: pass

def isDeadEnd(snake):
    global canIGoUp
    global canIGoDown
    global canIGoRight
    global canIGoLeft
    canIGoUpLeft = 1
    canIGoUpRight = 1
    canIGoDownLeft = 1
    canIGoDownRight = 1
    canIGoLeftDown = 1
    canIGoLeftUp = 1
    canIGoRightDown = 1
    canIGoRightUp = 1
    x1, y1 = snake[0]
    try:
        x2, y2 = snake[1]
    except:
        x2, y2 = snake[0]
    (headx, heady) = snake[0]# get the snake's head x and y position
    headlessTaillessSnake = snake[:] #Copy list
    del headlessTaillessSnake[0]
    if len(snake) == 1:
        pass
    else:
        pass
        del headlessTaillessSnake[(len(headlessTaillessSnake))-1]
    for bodyx, bodyy in headlessTaillessSnake:
        if y1 + 1 == bodyy and x1 - 1 == bodyx:
            canIGoUpLeft = 0
        elif y1 + 1 == bodyy and x1 + 1 == bodyx:
            canIGoUpRight = 0
        else: pass
    if canIGoUpLeft == 0 and canIGoUpRight == 0 and canIGoUp != 0 and canIGoUp != 1:
        canIGoUp = 2
    for bodyx, bodyy in headlessTaillessSnake:
        if y1 - 1 == bodyy and x1 - 1 == bodyx:
            canIGoDownLeft = 0
        elif y1 - 1 == bodyy and x1 + 1 == bodyx:
            canIGoDownRight = 0
        else: pass
    if canIGoDownLeft == 0 and canIGoDownRight == 0 and canIGoDown != 0 and canIGoDown != 1:
        canIGoDown = 2
    for bodyx, bodyy in headlessTaillessSnake:
        if x1 - 1 == bodyx and y1 + 1 == bodyy:
            canIGoLeftUp = 0
        elif x1 - 1 == bodyx and y1 - 1 == bodyy:
            canIGoLeftDown = 0
        else: pass
    if canIGoLeftDown == 0 and canIGoLeftUp == 0 and canIGoLeft != 0 and canIGoLeft != 1:
        canIGoLeft = 2
    for bodyx, bodyy in headlessTaillessSnake:
        if x1 + 1 == bodyx and y1 + 1 == bodyy:
            canIGoRightUp = 0
        elif x1 + 1 == bodyx and y1 - 1 == bodyy:
            canIGoRightDown = 0
        else: pass
    if canIGoRightDown == 0 and canIGoRightUp == 0 and canIGoRight != 0 and canIGoRight != 1:
        canIGoRight = 2
def howDoIGetToFood(snake):
    global canIGoUp
    global canIGoDown
    global canIGoRight
    global canIGoLeft
    headx, heady = snake[0]
    xfood, yfood = snakeFood.food[0]
    if xfood == headx:
        pass
    elif xfood < headx:
        if canIGoLeft == 0 or canIGoLeft == 1 or canIGoLeft == 2:
            print "kkk"
            pass
        else:
            canIGoLeft = 4
    elif xfood > headx:
        if canIGoRight == 0 or canIGoRight == 1 or canIGoRight == 2:
            print "kk"
            pass
        else:
            canIGoRight = 4
    else:
        print ("There has be an ai error")
    if yfood > heady:
        if canIGoUp == 0 or canIGoUp == 1 or canIGoUp == 2:
            pass
        else:
            canIGoUp = 4
    elif yfood < heady:
        if canIGoDown == 0 or canIGoDown == 1 or canIGoDown == 2:
            pass
        else:
            canIGoDown = 4
    else:
        print ("There has be an ai error")


def deadEnd():
    pass
