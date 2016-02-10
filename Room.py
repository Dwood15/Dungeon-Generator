#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random

class DimRange(object):
	def __init__(self, x1, x2, y1, y2):
		self.minX = x1
		self.maxX = x2
		self.minY = y1
		self.maxY = y2

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __eq__(self, rhs):
		return self.x == rhs.x and self.y == rhs.y
	
	def isVerticallyAligned(self, rhs):
		return self.x == rhs.x
		
	def isHorizontallyAligned(self, rhs):
		return self.y == rhs.y
		
class Hallway(object):
	def __init__(self,  sideA, sideB):
		#sideA will always be the far left or the topmost.
		#enforce alignment
		
		if(sideA.isVerticallyAligned(sideB)):
			self.isVertical = True
			if(sideA.x < sideB.x):
				self.pointA = sideA
				self.pointB = sideB
			else:
				self.pointA = sideB
				self.pointB = sideA
		else:
			if sideA.isHorizontallyAligned(sideB):
				self.isVertical = False
				if sideA.y < sideB.y:
					self.pointA = sideA
					self.pointB = sideB
				else:
					self.pointA = sideB
					self.pointB = sideA
			else:
				raise Exception('Hallway','Hallways can only be a line')
					
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
		
		if self.x1 > test.x2 or self.x2 < test.x1:
			return False
			
		if self.y1 > test.y2 or self.y2 < test.y1:
			return False
		'''
		if(self.isPointInside(test.x1, test.y1)) or (test.isPointInside(self.x1, self.y1)):
			return True

		if(self.isPointInside(test.x1, test.y2)) or (test.isPointInside(self.x1, self.y2)):
			return True

		if(self.isPointInside(test.x2, test.y1)) or (test.isPointInside(self.x2, self.y1)):
			return True

		if(self.isPointInside(test.x2, test.y2)) or (test.isPointInside(self.x2, self.y2)):
			return True
			
			
		#print "Our far left: %d their far right: %d"  %(self.x1, test.x1)
		
		#I've removed the point-by-point check because if the top 6 don't return 99% of the time
		#it's a bad room and we shouldn't be keeping it so it's probably bettter to just re roll it.
		
		#for x in xrange(self.x1 + 1, self.x1 + 3):
		#	for y in xrange(self.y1 + 1, self.y1 + 3):
		#		if test.isPointInside(x, y):
		#			return True
		print "Found an invalid room, but still passed it: (%d, %d)" %(self.y1, self.y2)	
		'''		
		return True