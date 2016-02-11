#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random
from Point import *
class DimRange(object):
	def __init__(self, x1, x2, y1, y2):
		self.min = Point(x1, y1)
		self.max = Point(y1, y2)


					
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
	
	def isPointInside(self, x, y):
		if((x >= TopLeft.x and x <= self.BotRight.x) and (y >= self.TopLeft.y and y <= self.BotRight.y)):
			return True
		else:
			return False
	#return true if there is intersection between this room
	# and another room - this tests to see if the top is lower than the lowest of the one to test.
	def intersects(self, test):
		return not (self.TopLeft.x > test.BotRight.x or self.BotRight.x < test.TopLeft.x or self.TopLeft.y > test.BotRight.y or self.BotRight.y < test.TopLeft.y)
			