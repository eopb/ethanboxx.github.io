#!/usr/bin/env python2

def computerAiMovement():
    global cantGoThere
    global snake_dir
    x, y = snake[0]
    try:
        x2, y2 = snake[1]
    except:
        x2, y2 = snake[0]
        #x2, y2 = "N/a", "N/a"
    pass
    (headx, heady) = snake[0]
    xfood, yfood = food[0]
    aiDirx = 0
    aiDiry = 0
    if xfood == headx:
        aiDirx = 0
    elif xfood > headx:
        aiDirx = 1
    elif xfood < headx:
        aiDirx = -1
    else:
        print ("There has be an ai error")
    if yfood == heady:
        aiDiry = 0
    elif yfood > heady:
        aiDiry = 1
    elif yfood < heady:
        aiDiry = -1
    else:
        print ("There has be an ai error")
    #print (str(aiDirx))
    #print (str(aiDiry))
    if aiDirx == 0 and aiDiry != 0:
        if (y + aiDiry != y2):
            snake_dir = (0, aiDiry)
            x1 = x
            y1 = y
            #for x , y in snake:
                #xdir, ydir = snake_dir
                #while (x1 + xdir == x and y1 + ydir == y) or (y1 + aiDiry == y2):
                    #print ("changing 4")
                    #changeDir()
                    #xdir, ydir = snake_dir
        else:
            print ("Cant go there 1")
            #x1 = x
            #y1 = y
            #for x , y in snake:
                #xdir, ydir = snake_dir
                #while (x1 + xdir == x and y1 + ydir == y) or (y1 + aiDiry == y2):
                    #print ("changing 3")
                    #changeDir()
                    #xdir, ydir = snake_dir
    elif aiDirx != 0 and aiDiry == 0:
        if (x + aiDirx != x2):
            snake_dir = (aiDirx, 0)
            #x1 = x
            #y1 = y
            #for x , y in snake:
                #xdir, ydir = snake_dir
                ##while (x1 + xdir == x and y1 + ydir == y) or (x1 + aiDirx == x2):
                    ##print "changing 2"
                    ##changeDir()
                    ##xdir, ydir = snake_dir
        else:
            print ("Cant go there 2")
            x1 = x
            y1 = y
            #for x , y in snake:
                #xdir, ydir = snake_dir
                #while (x1 + xdir == x and y1 + ydir == y) or (x1 + aiDiry == x2):
                    #print "changing 1"
                    #changeDir()
                    #xdir, ydir = snake_dir
    elif aiDirx != 0 and aiDiry != 0:
        directionRandom = randint(1, 2)
        if directionRandom == 1:
            if len(snake) == 1:
                snake_dir = (aiDirx, 0)
            else:
                if (x + aiDirx != x2):
                    snake_dir = (aiDirx, 0)
                    xdir, ydir = snake_dir
                    x1 = x
                    y1 = y
                    for x , y in snake:
                        if (x1 + xdir == x and y1 + ydir == y):
                            snake_dir = (0, aiDiry)
                            xdir, ydir = snake_dir
                else:
                    print ("Cant go there 3")
                    snake_dir = (0, aiDiry)
                #x, y = snake[0]
                #x1 = x
                #y1 = y
                #for x , y in snake:
                    #xdir, ydir = snake_dir
                    #while (x1 + xdir == x and y1 + ydir == y) or ((x1 + xdir == x2) and (y1 + ydir == y2)):
                        #print ("changing 8")
                        #changeDir()
                        #xdir, ydir = snake_dir
        else:
            if len(snake) == 1:
                snake_dir = (0, aiDiry)
            else:
                if (y + aiDiry != y2):
                    snake_dir = (0, aiDiry)
                    xdir, ydir = snake_dir
                    x1 = x
                    y1 = y
                    for x , y in snake:
                        if (x1 + xdir == x and y1 + ydir == y):
                            snake_dir = (aiDirx, 0)
                            xdir, ydir = snake_dir
                else:
                    print ("Cant go there 4")
                    snake_dir = (aiDirx, 0)
                x, y = snake[0]
                x1 = x
                y1 = y
                #for x , y in snake:
                    #xdir, ydir = snake_dir
                    #while (x1 + xdir == x and y1 + ydir == y) or ((y1 + ydir == y2) and (x1 + xdir == x2)):
                        #print ("changing 7")
                        #changeDir()
                        #xdir, ydir = snake_dir
    else:
        print ("There has be an ai error")
    xdir, ydir = snake_dir
    x1 = x
    y1 = y
    x, y = snake[0]
    x1 = x
    y1 = y
    cantGoThere = [(0,0)]
    for x , y in snake:
        #cantGoThere = [(0,0)]
        xdir, ydir = snake_dir
        while (x1 + xdir == x and y1 + ydir == y) or ((y1 + ydir == y2) and (x1 + xdir == x2)):
            print ("changing 7")
            cantGoThere.append((xdir, ydir))
            print (str(cantGoThere))
            changeDir()
            xdir, ydir = snake_dir
    #for x , y in snake:
        #while (x1 + xdir == x and y1 + ydir == y) or (xdir == 0 and ydir == 0) or (xdir == 1 and ydir == 1) or (xdir == -1 and ydir == -1) or (xdir == 1 and ydir == -1) or (xdir == -1 and ydir == 1):
            #xdir = randint(-1, 1)
            #ydir = randint(-1, 1)
            #snake_dir = (xdir, ydir)
        #else: pass
    return snake_dir

def changeDir():
    global snake_dir
    global cantGoThere
    cantGoTherex = []
    cantGoTherey = []
    xdir, ydir = snake_dir
    for x , y in cantGoThere:
        cantGoTherex.append(x)
        cantGoTherey.append(y)
    listchecks1 = 0
    while listchecks1 <  len(cantGoTherex):
        print ("khjaflkj" + str(len(cantGoTherex)) + "alkdfjalk" + str(listchecks1))
        #print str(listchecks)
        #print cantGoTherex
        while xdir == cantGoTherex[listchecks1] and ydir == cantGoTherey[listchecks1]:
            randomDir = randint(1,4)
            #print str(xdir)
            #print str(ydir)
            #print str(cantGoTherex)
            #print str(cantGoTherey)
            #print (str(randomDir))
            if randomDir == 1:
                snake_dir = (1, 0)
            elif randomDir == 2:
                snake_dir = (0, 1)
            elif randomDir == 3:
                snake_dir = (-1, 0)
            elif randomDir == 4:
                snake_dir = (0, -1)
            else:
                print ("Change error")
            xdir, ydir = snake_dir
        listchecks1 = listchecks1 + 1
    print (str(snake_dir))
    #return snake_dir
