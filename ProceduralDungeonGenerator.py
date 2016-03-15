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
MAX_ROOM_NUMBER = 4
MAX_DIST_FOR_HALLWAYS = 40

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
		
		self.hallways = []
		self.makeHallways(MAX_DIST_FOR_HALLWAYS)
		
	def __str__(self):
		return "\n".join(["".join(self._map[start:start + self.width]) for start in xrange(0, self.height * self.width, self.width)])
		
	def addRoomToString(self, room, ci):
		for i in [x + y * self.width for x in xrange(room.TopLeft.x, room.BotRight.x) for y in xrange(room.TopLeft.y, room.BotRight.y)]:
			self._map[i] = chr(ord(room.character)+ci)

	def addHallwaysToString(self):
		for l, item in enumerate(self.hallways):
			h = self.hallways[l]
			#print "Adding hallway: %d to string" %l,
			#print " Hallway verticality: " + str(h.isVertical)
			if(h.isVertical):
				for i in xrange(h.pointA.y - 1, h.pointB.y + 1):
					idx = (i * self.width) + h.pointA.x
					self._map[idx] = chr(ord('A')+l)
			else:
				for i in xrange(h.pointA.x - 1, h.pointB.x + 1):
					self._map[i + (h.pointA.y * self.width)] = chr(ord('A')+l)

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

        def getRoomProximities(self, i):
                #search for horizontal
		for j in xrange(0, MAX_ROOM_NUMBER):
			if i != j:
				#print 'Index i: {0:2d} Index j: {1:2d}'.format(i, j)
				sA = self.rooms[i].sharedAxis(self.rooms[j])
				p = self.rooms[i].findClosestWallsAndTheirDistances(self.rooms[j], sA)
				if p != None:
					self.proximities[i].append((j, p[0], p[1]))
                                        
                #print "Proximities found for room: %d with the following rooms:" %i
		self.proximities[i].sort(key=lambda x: (x[2], [1]))
		self.proximities[i] = self.removeRoomsNotInDirectLine(self.proximities[i])
		
		for p in xrange(0, len(self.proximities[i])):
			if self.proximities[i][p][1] == None:
                                del self.proximities[i][p]

        def shiftRoomLeft(self, i, leftMapWallDist):
                while(leftMapWallDist > self.rooms[i].getWidth() and len(self.proximities[i]) == 0):
                        self.rooms[i].shiftMe("Left")

        def shiftRoomRight(self, i, rightMapWallDist):
                while(rightMapWallDist > self.rooms[i].getWidth() and len(self.proximities[i]) == 0):
                        self.rooms[i].shiftMe("Right")
                        
        def shiftRoomLeftRight(self, i):
                leftMapWallDist = abs(1 - self.Rooms[i].TopLeft.x)
                rightMapWallDist = abs((self.width-1) - self.Rooms[i].BotRight.x)

                shiftRoomLeft(i, leftMapWallDist)
                shiftRoomRight(i, rightMapWallDist)

                if len(self.proximities[i] == 0):
                        print "Ran both left and right, and could not find a room"
                        
        def shiftRoomAsNeeded(self, i):
                if len(self.proximities[i]) > 0:
                        return
                elif MAX_ROOM_NUMBER == 1:
                        return
                
                topMapWallDist = abs(1 - self.Rooms[i].TopLeft.y)
                botMapWallDist = abs((self.height - 1) - self.Rooms[i].BotRight.y)

                if(topMapWallDist > botMapWallDist):
                        shiftUp = True

                if(shiftUp and not shiftedUp):
                        self.rooms[i].shiftMe("Up")
                elif (not shiftUp and not shiftedDown):
                        self.rooms[i].shiftMe("Down")
                else:
                        print "Ran both up and down, and could not find a room"
                               
	def buildAndSortProximities(self):
		#search horizontally
		self.proximities = []
                
		for i in xrange(0, MAX_ROOM_NUMBER):
			#list rooms in order of proximity.
			self.proximities.append([])
                        self.getRoomProximities(i)
                        self.shiftRoomAsNeeded(i)
                                
	def makeHallways(self, max_distance):
		#print "Making Hallways"
		for i in xrange(0, len(self.proximities)):
			for x in self.proximities[i]:
				if x[2] < max_distance and not self.rooms[i].sharesHallwayWith(x[0]):
					(ptA, ptB) = self.rooms[i].makeDoors(x[1], self.rooms[x[0]])
					self.rooms[i].addDoor(ptA, x[0])
					self.rooms[x[0]].addDoor(ptB, i)
					self.hallways.append(Hallway(ptA, ptB))
				
	def RollRoom(self, index):
		room = Room(self, minMaxRoomDims, index)
		return room 
		
		# def hallway(self, room1, room2, width):

if __name__ == '__main__':
	map = Map(80, 24)
	for x in xrange(0, MAX_ROOM_NUMBER):
		map.RollRoom(x)
		map.addRoomToString(map.rooms[x], x)

	map.addHallwaysToString()
	
	print map

	# Console 80 * 24
