import random
import time
import os
cols = 20
rows = 20
world = [[0 for j in range(cols)] for i in range(rows)]
episodes = 1000

def populate(world):
    '''
    Function to initialize a random space.
    '''
    for row,j in enumerate(world):
        for cols,_ in enumerate(j):
            if random.random()<0.5:
                world[row][cols] = 1

def get_neighbors(world,x,y):
    '''
    Function to return the number of neighbors(that are alive;1) for the specified cell 
    x -> row
    y -> column
                 1 1 0
	             0 0 1
                 0 0 1
    Number of neighbors should be 4.


    '''
    
    
    top = (x, y-1) if y != 0 else None
    top_right = (x+1, y-1) if y != 0 and x != len(world[0])-1 else None
    top_left = (x-1, y-1) if y != 0 and x != 0 else None
    bottom = (x, y+1) if y != len(world)-1 else None
    bottom_right = (x+1, y+1) if y != len(world)-1 and x != len(world[0])-1 else None
    bottom_left = (x-1, y+1) if y != len(world)-1 and x != 0 else None
    left = (x-1, y) if x != 0 else None
    right = (x+1, y) if x!= len(world[0])-1 else None
    
    neighbors = 0
    #print(bottom)
    if top != None:
        neighbors+=world[top[0]][top[1]]
    if top_right != None:
        neighbors+=world[top_right[0]][top_right[1]]
    if top_left != None:
        neighbors+=world[top_left[0]][top_left[1]]
    if bottom != None:
        neighbors+=world[bottom[0]][bottom[1]]
    if bottom_left != None:
        neighbors+=world[bottom_left[0]][bottom_left[1]]
    if bottom_right != None:
        neighbors+=world[bottom_right[0]][bottom_right[1]]
    if left != None:
        neighbors+=world[left[0]][left[1]]
    if right != None:
        neighbors+=world[right[0]][right[1]]
        
    return neighbors


def update(world):
    new_world = [[0 for j in range(len(world[0]))] for i in range(len(world))]
    
        
    """
    This function updates the world according to these rules:
		1. Any live cell with two or three live neighbours survives.
		2. Any dead cell with three live neighbours becomes a live cell.
		3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    """
    
    for row,j in enumerate(world):
        for col,k in enumerate(j):
            if (k == 1) and (get_neighbors(world, row, col) <2):
                new_world[row][col] = 0
            if (k == 1) and (get_neighbors(world, row, col) >3):
                new_world[row][col] = 0
            if (k == 1) and (get_neighbors(world, row, col) in [2,3]):
                new_world[row][col] = 1
            if (k == 0) and (get_neighbors(world,row,col) == 3):
                new_world[row][col] = 1
    return new_world
                
                
def print_world(world):
    os.system("cls")
    for i in world:
        for j in i:
            if j==1:
                print("\033[38;5;206m+",end="\033[0m ")
            elif j==0:
                print("+",end=" ")
        print("")
                
    time.sleep(0.5)


world = [
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,1,0],
    [0,1,0,1,1,1,0,0],
    [0,0,0,0,1,1,0,0],
    [0,0,0,1,1,0,0,0],
    [0,1,0,0,1,0,0,0],
    [1,0,1,0,0,1,0,0],
    [0,1,0,0,0,0,0,0],

]

generations = 100
print_world(world)

for i in range(generations):
    world = update(world)
    print_world(world)
