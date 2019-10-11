#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:55:05 2019

@author: bobo
"""

def slice_from(string,start,end):
    return string[start+1:end]

def reverse_string(string):
    return string[::-1]

    
print (slice_from('Hello',1,3))
print (reverse_string('Hello'))