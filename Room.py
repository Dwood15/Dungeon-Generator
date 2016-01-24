#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random

class Room(object):
    """docstring for Room"""
    def __init__(self, maxTop, maxLeft, top=None, left=None):
        self.width = random.randrange(4, 8)
        self.height = random.randrange(4, 8)
        if left == None:
        	self.left = random.randrange(1, maxLeft - self.width)
        else:
	        self.left = left
        if top == None:
        	self.top = random.randrange(1, maxTop - self.height)
        else:
	        self.top = top

