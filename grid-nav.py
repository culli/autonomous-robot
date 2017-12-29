#!/usr/bin/env python3
import time

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

robotDirection = SOUTH
ycoordinate = 0
xcoordinate = 0
sleepTime = 0.5


# grid = [  //works
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [1,1,1,1,1,0,1,1,1,1],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0]
# ]

grid = [
[0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0],
[0,1,1,0,1,0,0,0,0,0],
[0,0,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]
]

def isFacingSouth():
    global robotDirection, SOUTH
    return robotDirection == SOUTH

def moveForward():
    print('moveForward')
    global robotDirection, ycoordinate, xcoordinate, NORTH, SOUTH, EAST, WEST
    if (robotDirection == NORTH):
        ycoordinate = ycoordinate - 1
    if (robotDirection == EAST):
        xcoordinate = xcoordinate + 1
    if (robotDirection == SOUTH):
        ycoordinate = ycoordinate + 1
    if (robotDirection == WEST):
        xcoordinate = xcoordinate - 1

def turnRight():
    print('turnRight')
    global robotDirection
    robotDirection += 1
    if robotDirection > 3:
        robotDirection = 0

def turnLeft():
    print('turnLeft')
    global robotDirection
    robotDirection -= 1
    if robotDirection < 0:
        robotDirection = 3

def turnAround():
    print('turnAround')
    global robotDirection, NORTH, SOUTH, EAST, WEST
    if robotDirection == NORTH:
        robotDirection = SOUTH
    elif robotDirection == EAST:
        robotDirection = WEST
    elif robotDirection == SOUTH:
        robotDirection = NORTH
    elif robotDirection == WEST:
        robotDirection = EAST

def getFrontNumber():
    global NORTH, SOUTH, EAST, WEST
    newY = ycoordinate
    newX = xcoordinate

    if robotDirection == NORTH:
        newY = newY - 1

    if robotDirection == EAST:
        newX = newX + 1

    if robotDirection == SOUTH:
        newY = newY + 1

    if robotDirection == WEST:
        newX = newX - 1

    if (newX < 0 or newY < 0):
        return -1

    if newX >= len(grid[0]) or newY >= len(grid[0]):
        return -1

    return grid[newY][newX]

def getRightNumber():
    global NORTH, SOUTH, EAST, WEST
    print('getRightNumber {0} {1} {2}'.format(robotDirection, xcoordinate, ycoordinate))
    if robotDirection == NORTH:
        return grid[ycoordinate][xcoordinate + 1]

    if robotDirection == EAST:
        return grid[ycoordinate + 1][xcoordinate]

    if robotDirection == SOUTH:
        return grid[ycoordinate][xcoordinate - 1]

    if robotDirection == WEST:
        return grid[ycoordinate - 1][xcoordinate]

def getLeftNumber():
    global NORTH, SOUTH, EAST, WEST
    if robotDirection == NORTH:
        return grid[ycoordinate][xcoordinate - 1]

    if robotDirection == EAST:
        return grid[ycoordinate - 1][xcoordinate]

    if robotDirection == SOUTH:
        return grid[ycoordinate][xcoordinate + 1]

    if robotDirection == WEST:
        return grid[ycoordinate + 1][xcoordinate]

def isFrontOpen():
    global NORTH, SOUTH, EAST, WEST
    nextNumber = getFrontNumber()
    print('isFrontOpen {0}'.format(nextNumber))
    if nextNumber == 0:
        return True
    else:
        return False

def isRightOpen():
    global NORTH, SOUTH, EAST, WEST
    nextNumber = getRightNumber()
    print('isRightOpen {0}'.format(nextNumber))
    if nextNumber == 0:
        return True
    else:
        return False

def isLeftOpen():
    nextNumber = getLeftNumber()
    print('isLeftOpen {0}'.format(nextNumber))
    if nextNumber == 0:
        return True
    else:
        return False

def printGrid():
    global NORTH, SOUTH, EAST, WEST
    for i,row in enumerate(grid):
        for j,column in enumerate(row):
            if i == ycoordinate and j == xcoordinate:
                print 'X ',
            else:
                print '{0} '.format(grid[i][j]),
        print('')

print('start {0}'.format(grid[0][-10]))

lastX = xcoordinate
lastY = ycoordinate
while(True):
    print('x: {0}, y: {1}, dir: {2}'.format(xcoordinate, ycoordinate, robotDirection))

    if isFacingSouth() == False:
        turnRight()
        continue

    if isFrontOpen() == True:
        moveForward()
    else:
        turnLeft()
        if isFrontOpen() == True:
            moveForward()

    if (lastX == xcoordinate and lastY == ycoordinate):
        print 'robot stopped moving'
        break

    lastX = xcoordinate
    lastY = ycoordinate

    printGrid()
    time.sleep(sleepTime)
