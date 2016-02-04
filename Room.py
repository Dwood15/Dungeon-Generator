#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random

class Room(object):
    """docstring for Room"""
    def __init__(self, maxTop, maxLeft, top=None, left=None):
        self.width = random.randrange(6, 10)
        self.height = random.randrange(6, 10)
        if left == None:
        	self.left = random.randrange(0, maxLeft - self.width)
        else:
	        self.left = left
        if top == None:
        	self.top = random.randrange(0, maxTop - self.height)
        else:
	        self.top = top

