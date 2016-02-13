#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random
from Point import *

class Room(object):
	def __init__(self, map, minMaxRange):
		#far left of room - should always be the max range away from the outer wall
		x1 = random.randrange(1, (map.width - minMaxRange.max.x))
		#upper wall of room - same as above.
		y1 = random.randrange(1, (map.height - minMaxRange.max.y))
		self.TopLeft = Point(x1, y1)
		#Far right of room
		x2 = x1 + random.randrange(minMaxRange.min.x, minMaxRange.max.x + 1)

		#lower wall of room
		y2 = y1 + random.randrange(minMaxRange.min.y, minMaxRange.max.y + 1)
		self.BotRight = Point(x2, y2)
		self.HasHallway = False
	
	def isPointInside(self, x, y):
		if((x >= self.TopLeft.x and x <= self.BotRight.x) and (y >= self.TopLeft.y and y <= self.BotRight.y)):
			return True
		else:
			return False
	#return true if there is intersection between this room
	# and another room - this tests to see if the top is lower than the lowest of the one to test.
	def intersects(self, test):
		return not (self.TopLeft.x > test.BotRight.x or self.BotRight.x < test.TopLeft.x or self.TopLeft.y > test.BotRight.y or self.BotRight.y < test.TopLeft.y)
		
	#Find the wall closest to the one we're testing
	def findClosestWallsAndTheirDistances(self, test, vertical = False):
		if not vertical :
			#the higher it is, the firther to the right it is.
			if self.TopLeft.x > test.BotRight.x:
				return ("right", self.TopLeft.x - test.BotRight.x)
			else:
				return ("left", self.BotRight.x - test.TopLeft.x)
		else:
			#the higher the number it is, the lower it is
			if self.TopLeft.y > test.BotRight.y: 
				return ("lower", self.TopLeft.y - test.BotRight.y)
			else:
				return ("upper", self.BotRight.y - test.TopLeft.y)
				
	def sharesAxis(self, test):
		for i in xrange(self.TopLeft.y, self.BotRight.y + 1):
			if test.isPointInside(test.TopLeft.x, i):
				return ("x", self.BotRight.x - test.TopLeft.x)
		for i in xrange(self.TopLeft.x, self.BotRight.x + 1):
			if test.isPointInside(i, test.BotRight.y):
				return ("y", self.BotRight.x - test.TopLeft.x)
		return None