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

DIRECTIONS = ['right', 'left', 'upper', 'lower']
MAX_ROOM_NUMBER = 8

MIN_ROOM_X = 4
MAX_ROOM_X = 8
MIN_ROOM_Y = 4
MAX_ROOM_Y = 8

#A room should be 4x4 at the smallest, and 8x8 at largest
minMaxRoomDims = DimRange(MIN_ROOM_X, MIN_ROOM_Y, MAX_ROOM_X, MAX_ROOM_Y)


class Map(object):
	"""docstring for Map"""
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		#iterate over the map and fill it with wall tiles
		self._map = ["/" for i in xrange(0, width * height)] 

		self.rooms = [Room(self, minMaxRoomDims)] * MAX_ROOM_NUMBER
		
		for i in xrange(0, MAX_ROOM_NUMBER):
			self.rooms[i].myIndex = i
			#print "Testing to see if room: %d intersects with another room" %i
			while(self.isRoomIntersectingAnotherRoom(i)):
				self.rooms[i] = self.RollRoom(i)
		
		self.hallways = []
		self.findNearestRoomsAndMakeHallways()
				
	def __str__(self):
		return "\n".join(["".join(self._map[start:start + self.width]) for start in xrange(0, self.height * self.width, self.width)])
		
	def addRoomToString(self, room, ci):
		for i in [x + y * self.width for x in xrange(room.TopLeft.x, room.BotRight.x) for y in xrange(room.TopLeft.y, room.BotRight.y)]:
			self._map[i] = chr(ord(room.character)+ci)

	def addHallToString(self, hall):	
		vertPlus = 0
		horPlus = 0
		if hall.isVertical:
			vertPlus = 1
		else:
			horPlus = 1
		for i in [x + y * self.width for x in xrange(hall.pointA.x, hall.pointB.x + vertPlus) for y in xrange(hall.pointA.y, hall.pointB.y + horPlus)]:
			self._map[i] = ' '
			
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

	'''
	def traverseRoomsAndHallways(self, cameFrom=None, currentRoom=0):
		#start at room zero
		roomsTraversed = []
		if currentRoom != 0 and self.rooms[currentRoom].
			
			return roomsTraversed.fromList(self.traverseRoomsAndHallways(currentRoom, ) )
	'''
		
	#proximityList should NEVER include its own room in the list, so we shouldn't have to worry about that specific issue.
	#def createHallwayBetweenRooms(self, room_a, room_b, proximityList):	
	#	for p in proximityList:
	#		if p[0] == room_b and p[1] != None:
	def removeRoomsNotInDirectLine(self, proximities):
		savedProximities = []
		
		for d in DIRECTIONS:
			foundFirst = False
			for p in proximities:
				if p[1] == d  and not foundFirst:
					savedProximities.append(p)
					foundFirst = True
					
		return savedProximities
			
		
	def findNearestRoomsAndMakeHallways(self):
		#search horizontally
		proximities = []
		for i in xrange(0, MAX_ROOM_NUMBER):
			#list rooms in order of proximity.
			proximities.append([])
			
			#search for horizontal
			for j in xrange(0, MAX_ROOM_NUMBER):
				if i != j:
					#print 'Index i: {0:2d} Index j: {1:2d}'.format(i, j)
					baseProxim = self.rooms[i].findAxisWallsAndDistance(self.rooms[j])
					
					if baseProxim is not None:
						proximities[i].append((j, baseProxim[0], baseProxim[1]))
					
			print "Proximities found for room: %d with the following rooms:" %i

			tmpRange = len(proximities[i])
			
			if tmpRange > 0:
				#print sorted(self.proximities[i], key=lambda x: (x[2], [1]))
				proximities[i].sort(key=lambda x: (x[2], [1]))
				self.removeRoomsNotInDirectLine(proximities[i])
				print proximities[i]
			else:
				print "Room %d has no room in standard proximity!" %i
			
			for p in proximities[i]:
				if not self.rooms[i].hasHallwayWith(self.rooms[p[0]]):
						pointA = self.rooms[i].findAMatchingPoint(p[1], self.rooms[p[0]])
						pointB = self.rooms[p[0]].findClosestPoint(pointA)
						if  pointB is None:
							print "Failed to find matching point between rooms: {0:2d} and {0:2d}".format(i, p[0])
						else:
							self.hallways.append(Hallway(pointA, pointB, [i, p[0]]))
							hIdx = len(self.hallways)
							self.rooms[i].addHallway(hIdx)
							self.rooms[p[0]].addHallway(hIdx)
							
			
	def RollRoom(self, index):
		room = Room(self, minMaxRoomDims, index)
		return room 
		
		# def hallway(self, room1, room2, width):

if __name__ == '__main__':
	map = Map(80, 24)
	for x in xrange(0, MAX_ROOM_NUMBER):
		map.RollRoom(x)
		map.addRoomToString(map.rooms[x], x)

	for h in xrange(0, len(map.hallways)):
		map.addHallToString(map.hallways[h])
		
	print map

	# Console 80 * 24