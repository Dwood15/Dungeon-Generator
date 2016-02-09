#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random

class DimRange(object):
	def __init__(self, x1, x2, y1, y2):
		self.minX = x1
		self.maxX = x2
		self.minY = y1
		self.maxY = y2
			
class Room(object):
	def __init__(self, map, minMaxRange):
		#far left of room - should always be the max range away from the outer wall
		self.x1 = random.randrange(1, (map.width - minMaxRange.maxX))
		#upper wall of room - same as above.
		self.y1 = random.randrange(1, (map.height - minMaxRange.maxY))

		#Far right of room
		self.x2 = self.x1 + random.randrange(minMaxRange.minX, minMaxRange.maxX)

		#lower wall of room
		self.y2 = self.y1 + random.randrange(minMaxRange.minY, minMaxRange.maxY)
			
		
	def isPointInside(self, x, y):
		if((x >= self.x1 and x <= self.x2) and (y >= self.y1 and y <= self.y2)):
			return True
		else:
			return False
	#return true if there is intersection between this room
	# and another room
	def intersects(self, test):
	
		if(self.isPointInside(test.x1, test.y1)) or (test.isPointInside(self.x1, self.y1)):
			return True

		if(self.isPointInside(test.x1, test.y2)) or (test.isPointInside(self.x1, self.y2)):
			return True

		if(self.isPointInside(test.x2, test.y1)) or (test.isPointInside(self.x2, self.y1)):
			return True

		if(self.isPointInside(test.x2, test.y2)) or (test.isPointInside(self.x2, self.y2)):
			return True

		for x in xrange(self.x1, self.x2 + 1):
			for y in xrange(self.y1, self.y2 + 1):
				if test.isPointInside(x, y):
					return True
		return False;