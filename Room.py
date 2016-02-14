#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random
import sets

from Point import *

#A utility class for describing the range of sizes of rooms
class DimRange(object):
	def __init__(self, x1, y1, x2, y2):
		self.min = Point(x1, y1)
		self.max = Point(x2, y2)


class Room(object):
	def __init__(self, map, minMaxRange, index=0, char='a'):
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
		
		#my index from inside of the map class
		self.myIndex = index
		
		#If it has at least ONE hallway.
		self.HasHallway = False
		#just a list of indices.
		self.Hallways = []
		
		#the character which represents each room
		self.character = char
	
	def findMatchingRange(self, wall, roomB):
	
		if wall == 'left' or wall == 'right':
			sharedPoints = sets.Set(range(self.TopLeft.y, self.BotRight.y+1))
			sharedPoints &= sets.Set(range(roomB.TopLeft.y, roomB.BotRight.y+1))
	
		if wall == "upper" or wall == "lower":
			sharedPoints = sets.Set(range(self.TopLeft.x, self.BotRight.x + 1))
			sharedPoints &= sets.Set(range(roomB.TopLeft.x, roomB.BotRight.x + 1))

		return sharedPoints
			
	def findHallwayDirectlyBetween(self, test):
		for h in self.Hallways:
			if test.Hallways.index(h) != None:
				print "Found a hallway between: Room: {0:2d} and {0:2d}, hallway: {0:2d}".format(self.myIndex, test.myIndex, h)
				return (True, h)
		return (False, None, None)
		
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
				return ("upper", self.TopLeft.y - test.BotRight.y)
			else:
				return ("lower", self.BotRight.y - test.TopLeft.y)
				
	def sharesAxis(self, test):
		for i in xrange(self.TopLeft.y, self.BotRight.y + 1):
			if test.isPointInside(test.TopLeft.x, i):
				return self.findClosestWallsAndTheirDistances(test)
				
		for i in xrange(self.TopLeft.x, self.BotRight.x + 1):
			if test.isPointInside(i, test.BotRight.y):
				return self.findClosestWallsAndTheirDistances(test, True)
		return None