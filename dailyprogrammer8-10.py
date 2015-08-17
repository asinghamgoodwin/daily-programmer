#daily programmer easy challenge, square spirals

size = int(raw_input('what size grid?'))
user_number = raw_input("What do you want to find in the spiral? (either a number or a coordinate in the form of x y) ")

# targetNum = int(raw_input("which number are you looking for? "))
#coordinates =raw_input('which coordinates? (in the form 1 1)')
#print target

grid = [['+' for i in range(size)] for j in range(size)]

center = size/2

grid[center][center] = 1

counter = 1
direction = 0
currentLocation = (center, center) # (x, y)

transitionDict = {'right': (1, 0), 'left': (-1,0), 'up': (0,1), 'down': (0,-1)}

directionList = ['right', 'up', 'left', 'down']

for i in range(2, size**2+1):
    transition =  transitionDict[directionList[(direction+1) %4]]
    newX, newY = (currentLocation[0]+transition[0], currentLocation[1]+transition[1])
    
    currentX, currentY = currentLocation

    if grid[newX][newY] == '+':
        direction = (direction+1)%4
        grid[newX][newY] = i
        currentLocation = (newX, newY)

    else:
        continuation = transitionDict[directionList[direction]]
        nextX, nextY = (currentLocation[0]+continuation[0], currentLocation[1]+continuation[1])
        grid[nextX][nextY] = i
        currentLocation = (nextX, nextY)

#print grid

#figure out if the user_number is a coordinate or a plain number
if ' ' in user_number:
    # then coordinate
    target = (int(user_number[0])-1, int(user_number[-1])-1)
    print grid[target[0]][target[1]]
else:
    # plain number
    targetNum = int(user_number)
    for x in range(size):
        if targetNum in grid[x]:
           y = grid[x].index(targetNum)
           print (y+1, x+1)

#for row in grid:
#    print row
