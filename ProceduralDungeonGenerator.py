#!/usr/bin/env python
# -*-coding:Utf-8 -*

#external modules
import random

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
		self.room = [None] * MAX_ROOM_NUMBER

	def __str__(self):
		return "\n".join(["".join(self._map[start:start + self.width]) for start in xrange(0, self.height * self.width, self.width)])

	def addRoomToString(self, room):
		for i in [(x + y * self.width) for x in xrange(room.TopLeft.x, room.BotRight.x) for y in xrange(room.TopLeft.y, room.BotRight.y)]:
			self._map[i] = ' '

	def	isRoomIntersectingAnotherRoom(self, index):
		for i in xrange(0, MAX_ROOM_NUMBER):
			if (i != index) and (self.room[index] != None) and (self.room[i] != None):
				if (self.room[index].intersects(self.room[i])):
					return True
			#Depends on the linear insertion into the room array object
			if(self.room[index] == None):
				return False
		return False

	def MakeHallway(self, roomAIndex, roomBIndex):
		pass
		
	def RollRoom(self, index, maxReRolls= -1):
		reRoll = 1
		self.room[index] = Room(self, minMaxRoomDims)

		while(self.isRoomIntersectingAnotherRoom(index) and maxReRolls != reRoll):
			reRoll = reRoll + 1
			self.room[index] = Room(self, minMaxRoomDims)
		
		return maxReRolls != reRoll 
		
		# def hallway(self, room1, room2, width):

if __name__ == '__main__':
	map = Map(80, 24)
	for x in xrange(0, MAX_ROOM_NUMBER):
		map.RollRoom(x)
		map.addRoomToString(map.room[x])

	print map

	# Console 80 * 24