"""
CSSE1001 2019s2a1
"""
from a1_support import *


# Write the expected functions here
def get_position_in_direction(position, direction):
    """
    get current position, and direction from input, 
    then  the next position in direction
    """
    #the type of the position is tuple, like the inital (0, 1)
    #give the first value to x, and second value to y
    x, y = position
    #the type of direction_value is tuple, 
    #we get the value from "DIRECTIONS" in a1_support by matching the keys(direction) and values 
    direction_value = DIRECTIONS[direction]
    xi, yi = direction_value
    position = (x+xi, y+yi)
    return position 
    #returns like (0,1) tuple


def get_tile_at_position(level, position):
    """
    this function is used to get the tile of the current position
    """
    #use the function "level_size" from a1_support to get the map size :example:tuple (1, -1)
    size = level_size(level)
    #use the function "position_to_index" from a1_support to get the current position in map
    #for example, the initial position(0, 1)'s index is 152, the type is int
    #cuz the type of level(map) is string, we need to use string[] to find the corresponding tile(type:str) in the map
    index = position_to_index(position, size)
    if level[index] == AIR:
        tile = AIR
    elif level[index] == COIN:
        tile = COIN
    elif level[index] == PLAYER:
        tile = PLAYER
    elif level[index] == WALL:
        tile = WALL
    elif level[index] == GOAL:
        tile = GOAL
    elif level[index] == CHECKPOINT:
        tile = CHECKPOINT
    elif level[index] == MONSTER:
        tile = MONSTER
    return tile
    #the return type of tile is string, used the value's name(AIR, COIN, etc.) 
    #which defined in a1_support to represent the string


def get_tile_in_direction(level, position, direction):
    """
    once we defined the get_position_in_direction and get_tile_at_position function,
    we can use them to get the tile in new position
    """
    #functions instantiation
    position = get_position_in_direction(position, direction)
    tile = get_tile_at_position(level, position)
    return tile
    #return tile, types string


def remove_from_level(level, position):
    """
    the purpose of this function is to rm the tile from the target position
    but we cant directly operate on string object,so I choose to cast string to list
    """
    #functions from a1_support to get size(int) of the map(string) and index(int)
    size = level_size(level)
    index = position_to_index(position, size)
    #use list() to cast object to list
    level_list = list(level)
    #use AIR:' ' to replace the previous tile at this position
    level_list[index] = AIR
    #convert level_list to level(string)
    level = ''.join(level_list)
    return level
    # return removed-map (type str)


def print_level(level, position):

    """
    this function is for print the map
    """    
    #get the current map's size
    size = level_size(level)
    #instantiate the position_to_index function to get this position's index value
    index = position_to_index(position, size)
    #convert str to list.
    level_list = list(level)
    #use PLAYER to replace the previous tile at this position 
    level_list[index] = PLAYER
    level = ''.join(level_list)
    print(level)


def move(level, position, direction):
    """
    the purpose of this function is to move the player to the position in direction which you just typed in
    so we need to consider two scenarios : 1.the tile in direction position is WALL  2. the tile in direction position is AIR.
    based on scenario 1: according to the assignment instruction: next step is to go up 
                         and check if the tile at the new positon is air, if so, return new position
    based on scenario 2: next step have two cases
                         case1: if the tile below next tile is AIR then go down and then return the new position
                         case2: if the tile below next tile is not AIR then return the new position in direction without go down
    """
    if get_tile_in_direction(level, position, direction) == AIR or get_tile_in_direction(level, position, direction) == WALL:
        while(True):
            if get_tile_in_direction(level, position, direction) == WALL:
                position = get_position_in_direction(position, UP)
                if get_tile_in_direction(level, position, direction) == AIR:                
                    position = get_position_in_direction(position, direction)
                    return position

            elif get_tile_in_direction(level, position, direction) == AIR: 
                new_position = get_position_in_direction(position, direction)
                if get_tile_in_direction(level, new_position, DOWN) == AIR:
                    position = get_position_in_direction(position, DOWN)
                elif get_tile_in_direction(level, new_position, DOWN) != AIR:
                    position = get_position_in_direction(position, direction)
                    return position
               
    else:
        position = get_position_in_direction(position, direction)
        return position


def attack(level, position):
    """
    this function is for attack the monster
    """ 
    #case 1: if the position to the left of the player is a monster
    if get_tile_in_direction(level, position, LEFT) == MONSTER:
        print('Attacking the monster on your left!')
        #get the position of monster
        position = get_position_in_direction(position, LEFT)
        #remove the Monster
        level = remove_from_level(level, position)
        #then return the new level
        return level
    #case 2: if the position to the right of the player is a monster
    elif get_tile_in_direction(level, position, RIGHT) == MONSTER:
        print('Attacking the monster on your right!')
        #get the position of monster
        position = get_position_in_direction(position, RIGHT)
        level = remove_from_level(level, position)
        return level
    #case 3: if neither side of the player is a monster
    else:
        print('No monsters to attack!')
        return level

    


def tile_status(level, position):
    """
    this function is for print status
    """ 
    tile = get_tile_at_position(level, position)
    if tile == GOAL:
        print("Congratulations! You finished the level")
        #break
    elif tile == MONSTER:
        print("Hit a monster!")
    elif tile == COIN or tile == CHECKPOINT:
        level = remove_from_level(level, position)   
    status = (tile, level)
    return status



def main():
    """
    this function is the main function
    """ 
    #initial score
    score = 0
    #initial position
    position = (0, 1)
    
    #initial checkpoint vars to save status
    checkpoint = ()
    savescore = ''
    savemap = ''
    
    #input file name
    file_name = str(raw_input('Please enter the name of the level file (e.g. level1.txt): '))
    # add player to the level
    level = load_level(file_name)
    
    #main loop
    while(True):
        #print score
        print('Score: '+ str(score))
        #print level
        print_level(level, position)
        #get actions
        action = str(raw_input("Please enter an action (enter '?' for help): "))
        
        if action == '?' or action == 'help':
            print(HELP_TEXT)
        elif action == 'q':
            break
        elif action == RIGHT or action == LEFT:
            position = move(level, position, action)
            tile, level = tile_status(level, position)
            if tile == COIN:
                score +=1
            elif tile == GOAL:
                break
            elif tile == CHECKPOINT:
                checkpoint = position
                savescore = score
                savemap = level
            elif tile == MONSTER:
                if checkpoint:
                    position = checkpoint
                    score = savescore
                    savemap = level
                else:
                    break                         
        elif action == 'a':
            level = attack(level, position)
        elif action == 'n':
            if checkpoint:
                position = checkpoint
                score = savescore
                savemap = level


if __name__ == "__main__":
    main()
    
    
    
