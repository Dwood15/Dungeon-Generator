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
MAX_ROOM_NUMBER = 22

MIN_ROOM_X = 4
MAX_ROOM_X = 8
MIN_ROOM_Y = 4
MAX_ROOM_Y = 8

#A room should be 4x4 at the smallest, and 8x8 at largest
minMaxRoomDims = DimRange(MIN_ROOM_X, MAX_ROOM_X, MIN_ROOM_Y, MAX_ROOM_Y)


class Map(object):
	"""docstring for Map"""
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		#iterate over the map and fill it with wall tiles
		self._map = ["#" for i in xrange(0, width * height)] 
		self.rooms = [Room(self, minMaxRoomDims)] * MAX_ROOM_NUMBER
		for i in xrange(0, MAX_ROOM_NUMBER):
			print "Testing to see if room: %d intersects with another room" %i
			while(self.isRoomIntersectingAnotherRoom(i)):
				self.rooms[i] = self.RollRoom(i)
				
	def __str__(self):
		return "\n".join(["".join(self._map[start:start + self.width]) for start in xrange(0, self.height * self.width, self.width)])

	def addRoomToString(self, room):
		for i in [(x + y * self.width) for x in xrange(room.TopLeft.x, room.BotRight.x) for y in xrange(room.TopLeft.y, room.BotRight.y)]:
			self._map[i] = ' '

	def	isRoomIntersectingAnotherRoom(self, index):
		for i in xrange(0, MAX_ROOM_NUMBER):
			#'''and (self.rooms[index] != None)''' 
			if (i != index) and (self.rooms[i] != None):
				if (self.rooms[index].intersects(self.rooms[i])):
					return True
			#Depends on the linear insertion into the room array object
			if(self.rooms[index] == None):
				return False
		return False

	def FindNearestRoomsAndMakeHallways(self):
		#search horizontally
		self.proximities = []
		
		for i in xrange(0, MAX_ROOM_NUMBER + 1):
			#list rooms in order of proximity.
			self.proximities.append([])
			
			#search for horizontal
			for j in xrange(0, MAX_ROOM_NUMBER + 1):
				if i != j:
					print 'Index i: {0:2d}{1:2d} Index j: %d'.format(i, j)
					self.proximities[i].append((j, self.rooms[i].sharesAxis(self.rooms[j])))

			for j in xrange(0, MAX_ROOM_NUMBER + 1):
				if i != j:
					self.proximities[i].append((j, self.rooms[i].sharesAxis(self.rooms[i])))
					
			print "Proximities found for room: %d with the following rooms:" %i
			for p in self.proximities:
				print "%d, %s" %p[0] %p[1][0]
			
			
	#index_a and b are the indexes to the two rooms we want to match up.
	def MakeHallway(self, index_a, index_b, Vertical = False):
		AvailablePoints = []
		if(Vertical):
			self.rooms[index_a].sharesAxis(index_b)
			AvailablePoints.append(X)
		else:
			for Y in xrange(self.rooms[index_a].TopLeft.y, self.rooms[index_a].BotRight.y + 1):
				if self.rooms[index_b].isPointInside(Y, self.rooms[index_b].BotRight.x):
					AvailablePoints.append(Y)
				
		for i in AvailablePoints:
			if Vertical:
				print "Vertical room, roomA: %d" 
			print "Available  Point: %d" %i
		
		
	def RollRoom(self, index):
		room = Room(self, minMaxRoomDims)
		return room 
		
		# def hallway(self, room1, room2, width):

if __name__ == '__main__':
	map = Map(80, 24)
	for x in xrange(0, MAX_ROOM_NUMBER):
		map.RollRoom(x)
		map.FindNearestRoomsAndMakeHallways()
		map.addRoomToString(map.rooms[x])

	print map

	# Console 80 * 24