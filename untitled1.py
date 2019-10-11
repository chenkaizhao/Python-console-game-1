#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:13:41 2019

@author: bobo
"""
from a1_support import *

def get_position_in_direction(position, direction):
    """
    get current position, and direction from input, 
    then  the next position in direction
    """
    x, y = position
    direction_value = DIRECTIONS[direction]
    print(type(direction_value))
    xi, yi = direction_value
    position = (x+xi, y+yi)
    #position = 
    # convert the direction to position, according to the dict("DIRECTIONS" located in al_support)
    #if direction  == a1s.DIRECTIONS.keys():
         #direction = a1s.DIRECTIONS[direction]
    #elif direction == 'a':
        
    #
    #new_position = [position[i]+list(direction)[i] for i in range(len(position))]
    return position 
    #return list like [0,1]

position = (0, 1)
print(get_position_in_direction(position, 'r'))

def get_tile_at_position(level, position):
    #use the function "level_size" from a1_support to get the map size :example:232 
    size = level_size(level)
    
    #level_list = list(level)
    
    #use the function "position_to_index" from a1_support to get the current position in map
    #the initial position(0, 1)'s index is 152, the type is int
    #cuz the level map type is string, we need to use string[] to find the corresponding string(tile) in the map
    index = position_to_index(position, size)
    if level[index] == AIR:
        tile = AIR
    elif level[index] == COIN:
        tile = a1s.COIN
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

level = load_level('level1.txt')
print(type(get_tile_at_position(level, position)))


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
    #use AIR:' ' to replace the previous tile
    level_list[index] = AIR
    level_list = ''.join(level_list)
    print(type(level_list))
    remove_level = str(level_list) 
    print(type(remove_level))
    return remove_level
    # return level string
#remove_from_level(level, position)

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

def move(level, position, direction):
    if get_tile_in_direction(level, position, direction) == AIR or get_tile_in_direction(level, position, direction) == WALL:
        while True:
            if get_tile_in_direction(level, position, direction) != AIR:
                level = remove_from_level(level, position)
                new_position = get_position_in_direction(position, UP)
                if get_tile_at_position(level, new_position) == AIR:
                    return new_position
                elif get_tile_at_position(level, new_position) != AIR:
                    new_position = get_position_in_direction(position, DOWN)
                    return new_position
        position = new_position
    return level, position
    #return level string and updated position

move(level, position, direction)
    
    
    
