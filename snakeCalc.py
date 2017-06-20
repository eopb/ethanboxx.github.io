#!/usr/bin/env python2
from random import randint
import time
import var
import snakeAi
import snakeFood


def spawnSnakes():
    global foodToAppend
    global printmessage
    foodToAppend = False
    printmessage = "Loading"

    global snakes
    global score
    global snake_dir
    global startTime2
    global endGame
    endGame = False
    startTime2 = time.time()
    snake_dir = (1, 0)  # snake movement direction
    score = 0
    snakes = []
    intisualNumberOfSnakes = var.numberOfSnakes
    while var.numberOfSnakes > 0:
        positionx = int((var.field_width/intisualNumberOfSnakes)*var.numberOfSnakes)
        positiony = int((var.field_height/intisualNumberOfSnakes)*var.numberOfSnakes)
        snakes.append([((positionx), (positiony))])
        var.numberOfSnakes = var.numberOfSnakes - 1
    var.numberOfSnakes = intisualNumberOfSnakes
    print (str(snakes))

def repeatScript():
    global startTime
    startTime = time.time()
    global foodToAppend
    global score
    global endGame
    global SnakeHue
    global headx
    global heady
    global food

    # TODO update things...
    for snake in snakes:
        #if foodToAppend:
            #snake.append((headx, heady))
            #foodToAppend = False
        #else:
            #pass
        moveSnake(snake)
        #snake.insert(0, vec_add(snake[0], snake_dir))
        #snake.pop()
        # let the snake eat the food
        print ("Snakes body is in tiles "+str(snake))
        #headlessSnake.pop(0)
        checkWallCode(snake)
        copyOfSnake = snake[:]
        cutOffHead(snake)
        snakeindex = -1
        for snake in snakes:
            (headx, heady) = snake[0]# get the snake's head x and y position
            headlessSnake = snake[:] #Copy list
            del headlessSnake[0]
            if len(snakes) == 1:
                for x, y in headlessSnake:
                    if headx == x and heady == y:
                        printmessage = "Game over! Your score was " + str(score)
                        print ("Game over! Your score was " + str(score))
                        endGame = True
                    else:
                        pass
            if snake == copyOfSnake:
                for x, y in headlessSnake:
                    if headx == x and heady == y:
                        printmessage = ("Game over! Your score was " + str(score))
                        print ("Game over! Your score was " + str(score))
                        endGame = True
                        print (str(time.time() - startTime2))
                    else:
                        pass
            else: pass
        for snake in snakes:
            for x, y in snakeFood.food:            # go through the food list
                (headx, heady) = snake[0]
                if headx == x and heady == y:  # is the head where the food is?
                    print ("The snake ate food at [" + str(x) + "," + str(y) + "]. The snake will get longer.")
                    foodToAppend = True
                    #snake.append((x, y)) # make the snake longer
                    snakeFood.food.remove((x, y))  # remove the food
                    snakeFood.spawnFood(snake)
                    score = score + 1
                    printmessage = str("Your score is " + str(score))
                    headx = x
                    heady = y
    #print (str((time.time() - startTime) * 1000000))
    #time.sleep()
def moveSnake(snake):
    global foodToAppend
    global snake_dir
    global aiToSetUp
    global headx
    global heady
    if foodToAppend:
        snake.append((headx, heady))
        foodToAppend = False
    else:
        pass
    if var.computerAi:
        #snake_dir = computerAiMovement()
        #computerAiMovement()
        snake_dir = snakeAi.computerAiMovement2(snake)
    else: pass

    aiToSetUp = False
    howLong = len(snake) # Get the length of the snake.
    dirx, diry = snake_dir # Get the snakes direction.
    (headx, heady) = snake[0] # Get the snakes head.
    del snake[(howLong - 1)] # Remove the end of the snakes tail.
    snake.insert(0, (headx + dirx, heady + diry)) # Add a new head at the direction side of the new one.
    #return snake
    #if computerAi and (aiToSetUp == False):
        #snake_dir = computerAiMovement()
    #else: pass
    return snake

def checkWallCode(snake):
    global xprotect
    global yprotect
    snakeindex = -1
    for x, y in snake:
        xprotect = "Protected"
        yprotect = "Protected"
        snakeindex = snakeindex + 1
        if x == xprotect and y == yprotect:
            xprotect = "Protected"
            yprotect = "Protected"
        else:
            if x < 0:
                xprotect, yprotect = x, y
                snake.remove((x, y))
                snake.insert(snakeindex, ((var.field_width-1), y))
                print ("Snake body part at " + str(x) + "," + str(y) + " has gone through a wall.")
                print ("It has been moved to " + str(var.field_width) + "," + str(y) +".")
            elif x >= (var.field_width):
                xprotect, yprotect = x, y
                snake.remove((x, y))
                snake.insert(snakeindex, (0, y))
                print ("Snake body part at [" + str(x) + "," + str(y) + "] has gone through a wall. It has been moved to [1," + str(y) +"].")
            elif y < 0:
                xprotect, yprotect = x, y
                snake.remove((x, y))
                snake.insert(snakeindex, (x, (var.field_height-1)))
                print ("Snake body part at [" + str(x) + "," + str(y) + "] has gone through a wall. It has been moved to [" + str(x) + "," + str(var.field_height) +"].")
            elif y >= (var.field_height):
                xprotect, yprotect = x, y
                snake.remove((x, y))
                snake.insert(snakeindex, (x, 0))
                print ("Snake body part at [" + str(x) + "," + str(y) + "] has gone through a wall. It has been moved to [" + str(x) + ",1].")
    return snake


def cutOffHead(snake):
    (headx, heady) = snake[0]# get the snake's head x and y position
    headlessSnake = snake[:] #Copy list
    del headlessSnake[0]
    return headlessSnake
