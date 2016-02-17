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
		self.hasHallway = False
		
		#just a list of indices + the point the hallway starts at
		self.hallways = []
		
		#the character which represents each room
		self.character = char
	
	
	def isPtInVerticalRange(self, pt):
		return pt.x <= self.BotRight.x and pt.x >= self.TopLeft.x
	
	def isPtInHorizontalRange(self, pt):
		return pt.y <= self.BotRight.y and pt.y >= self.TopLeft.y
	
	def findClosestPoint(self, pt):
		if(self.isPtInHorizontalRange(pt)) or self.isPtInVerticalRange(pt):
			dir = self.findDirectionOfPointFromRoom(pt)
			if dir == 'right':
				return Point(self.BotRight.x, pt.y)
			if dir == 'left':
				return Point(self.TopLeft.x, pt.y)
			if dir == 'upper':
				return Point(pt.x, self.TopLeft.y)
			if dir == 'lower':
				return Point(pt.x, self.BotRight.y)
			#if it's inside of the thing, we return the same dealio
			return pt
		else:
			#We can only handle four of the cardinal directions, not all 8
			print "Point: " + str(pt) + "Is not in a direct line"
			return None
	
	#technically a private function I believe
	def findDirectionOfPointFromRoom(self, pt):
			if pt.x > self.BotRight.x:
				return 'right'
			if pt.y > self.BotRight.y:
				return 'lower'
			if pt.x < self.TopLeft.x:
				return 'left'
			if pt.y < self.TopLeft.y:
				return 'upper'
			if self.isPointInside(pt.x, pt.y):
				return 'inside'
		
	def shiftRoom(direction, range):
		range = random.randrange(1, range)
		print "Attempting to shift range!"
		
		if direction == 'left':
			self.TopLeft.x - range
		if direction == 'upper':
			self.TopLeft.y - range
		if direction == 'lower':
			self.BotRight.x + range
		if direction == 'right':
			self.BotRight.x + range
			
	def addHallway(self, hallwayIndex):
		if not self.hasHallway:
			self.hasHallway = True
		self.hallways.append(hallwayIndex)
	
	def hasHallwayWith(self, room):
		tmpHallways = sets.Set(self.hallways)
		tmpHallways &= sets.Set(room.hallways)
		return len(tmpHallways) > 0
		
	def findAMatchingPoint(self, wall, roomB):
	
		if wall == 'left' or wall == 'right':
			sharedPoints = sets.Set(range(self.TopLeft.y, self.BotRight.y+1))
			sharedPoints &= sets.Set(range(roomB.TopLeft.y, roomB.BotRight.y+1))
	
		if wall == "upper" or wall == "lower":
			sharedPoints = sets.Set(range(self.TopLeft.x, self.BotRight.x + 1))
			sharedPoints &= sets.Set(range(roomB.TopLeft.x, roomB.BotRight.x + 1))
		
		if sharedPoints is None:
			return None
			
		ptReturn = random.choice(tuple(sharedPoints)) 
		print "Points in common: " + str(sharedPoints),
		print " ptReturn : {0:2d}".format(ptReturn)
		
		if wall == 'left':
			pt = Point(self.TopLeft.x, ptReturn)
		if wall == 'right':
			pt = Point(self.BotRight.x, ptReturn)
		if wall == 'upper':
			pt = Point(ptReturn, self.TopLeft.y)
		if wall == 'lower':
			pt = Point(ptReturn, self.BotRight.y)
		
		print "FindAMatchingPoint: " + str (pt)
		return  pt
			
	def findHallwaysDirectlyBetween(self, test):
		h = self.Hallways
		h &= test.Hallways
			
		num = len(h)

		if num != 0:
				print "Found a hallway between: Room: {0:2d} and {0:2d}, hallway: {0:2d}".format(self.myIndex, test.myIndex, h[0])
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
		return not (self.TopLeft.x >= test.BotRight.x or self.BotRight.x <= test.TopLeft.x 
					or self.TopLeft.y >= test.BotRight.y or self.BotRight.y <= test.TopLeft.y)
		
	#Find the wall closest to the one we're testing
	def findClosestWallsAndTheirDistances(self, test, vertical = False):
		if not vertical :
			#the higher it is, the firther to the right it is.
			if self.TopLeft.x > test.BotRight.x:
				return ("left", abs(self.TopLeft.x - test.BotRight.x))
			else:
				return ("right", abs(self.BotRight.x - test.TopLeft.x))
		else:
			#the higher the number it is, the lower it is
			if self.TopLeft.y > test.BotRight.y: 
				return ("upper", abs(self.TopLeft.y - test.BotRight.y))
			else:
				return ("lower", abs(self.BotRight.y - test.TopLeft.y))
				
	def findAxisWallsAndDistance(self, test):
		for i in xrange(self.TopLeft.y, self.BotRight.y + 1):
			if test.isPointInside(test.TopLeft.x, i):
				return self.findClosestWallsAndTheirDistances(test)
				
		for i in xrange(self.TopLeft.x, self.BotRight.x + 1):
			if test.isPointInside(i, test.BotRight.y):
				return self.findClosestWallsAndTheirDistances(test, True)
		return None