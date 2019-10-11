#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:04:23 2019

@author: bobo
"""
from a1_support import *

def get_tile_at_position(level, position):
    """
    this function is used to get the tile of the current position
    """
    #use the function "level_size" from a1_support to get the map size :example:232 str 
    s = level_size(level)
    #use the function "position_to_index" from a1_support to get the current position in map
    #for example, the initial position(0, 1)'s index is 152, the type is int
    #cuz the type of level(map) is string, we need to use string[] to find the corresponding tile(type:str) in the map
    i = position_to_index(position, s)
    if level[i] == AIR:
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
    
get_tile_at_position('level1.txt', (0, 1))