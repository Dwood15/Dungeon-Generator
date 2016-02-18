#!/usr/bin/env python
# -*-coding:Utf-8 -*

#external modules
import random
from array import *

#our modules/files
from Point import *
from Room import *
from Hallway import *

#Move min max to own named variables
#Min room #, max room #
MAX_ROOM_NUMBER = 8

MIN_ROOM_X = 4
MAX_ROOM_X = 8
MIN_ROOM_Y = 4
MAX_ROOM_Y = 8

#A room should be 4x4 at the smallest, and 8x8 at largest
minMaxRoomDims = DimRange(MIN_ROOM_X, MIN_ROOM_Y, MAX_ROOM_X, MAX_ROOM_Y)
DIRECTIONS = ['right', 'left', 'upper', 'lower']

class Map(object):
	"""docstring for Map"""
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		#iterate over the map and fill it with wall tiles
		self._map = ["-" for i in xrange(0, width * height)] 

		self.rooms = [Room(self, minMaxRoomDims)] * MAX_ROOM_NUMBER
		
		for i in xrange(0, MAX_ROOM_NUMBER):
			self.rooms[i].myIndex = i
			#print "Testing to see if room: %d intersects with another room" %i
			while(self.isRoomIntersectingAnotherRoom(i)):
				self.rooms[i] = self.RollRoom(i)
				
		self.proximities = []
		self.buildAndSortProximities()
				
		self.makeHallways()
	def __str__(self):
		return "\n".join(["".join(self._map[start:start + self.width]) for start in xrange(0, self.height * self.width, self.width)])
		
	def addRoomToString(self, room, ci):
		for i in [x + y * self.width for x in xrange(room.TopLeft.x, room.BotRight.x) for y in xrange(room.TopLeft.y, room.BotRight.y)]:
			self._map[i] = chr(ord(room.character)+ci)

	def isRoomIntersectingAnotherRoom(self, index):
		for i in xrange(0, MAX_ROOM_NUMBER):
			#'''and (self.rooms[index] != None)''' 
			if (i != index) and (self.rooms[i] != None):
				if (self.rooms[index].intersects(self.rooms[i])):
					return True
			#Depends on the linear insertion into the room array object
			if(self.rooms[index] == None):
				return False
		return False
		
	def removeRoomsNotInDirectLine(self, proximities):
		savedProximities = []
		
		for d in DIRECTIONS:
			foundFirst = False
			for p in proximities:
				if p[1] == d  and not foundFirst:
					savedProximities.append(p)
					foundFirst = True
					
		return savedProximities
		
	def buildAndSortProximities(self):
		#search horizontally
		self.proximities.clear()
		
		for i in xrange(0, MAX_ROOM_NUMBER):
			#list rooms in order of proximity.
			self.proximities.append([])
			
			#search for horizontal
			for j in xrange(0, MAX_ROOM_NUMBER):
				if i != j:
					#print 'Index i: {0:2d} Index j: {1:2d}'.format(i, j)
					sA = self.rooms[i].sharedAxis(self.rooms[j])
					p = self.rooms[i].findClosestWallsAndTheirDistances(self.rooms[j], sA)
					if p != None:
						self.proximities[i].append((j, p[0], p[1]))
					
			print "Proximities found for room: %d with the following rooms:" %i
			self.proximities[i].sort(key=lambda x: (x[2], [1]))
			self.proximities[i] = self.removeRoomsNotInDirectLine(self.proximities[i])
			
			for p in xrange(0, len(self.proximities[i])):
				if self.proximities[i][p][1] == None: #and p[1][0] != None:
					del self.proximities[i][p]
				#else:
				#	print self.proximities[i][p]
			
	def makeHallways(self, max_distance):
		print "Making Hallways"
		for i in xrange(0, len(self.proximities)):
			for x in self.proximities[i]:
				if x[2] < 15:
					(ptA, ptB) = self.rooms[i].makeDoors(x[1], self.rooms[x[0]])
					self.rooms[i].addDoor(pt)
					self.rooms[x[0]].addDoor(ptB)
				
	def RollRoom(self, index):
		room = Room(self, minMaxRoomDims, index)
		return room 
		
		# def hallway(self, room1, room2, width):

if __name__ == '__main__':
	map = Map(80, 24)
	for x in xrange(0, MAX_ROOM_NUMBER):
		map.RollRoom(x)
		map.addRoomToString(map.rooms[x], x)

	print map

	# Console 80 * 24