#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random
from Room import *



minMaxRoomDims = DimRange(4, 8, 4, 8)


		
class Map(object):
	"""docstring for Map"""
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		#iterate over the map and fill it with wall tiles
		self._map = ["#" for i in xrange(0, width * height)] 
		self.room = [None] * 8

	def __str__(self):
		return "\n".join(["".join(self._map[start:start + self.width]) for start in xrange(0, self.height * self.width, self.width)])

	def addRoomToString(self, room):
		for i in [(x + y * self.width) for x in xrange(room.x1, room.x2) for y in xrange(room.y1, room.y2)]:
			self._map[i] = ' '

	def	isRoomIntersectingAnotherRoom(self, index):
		for i in xrange(0, 8):
			if (i != index) and (self.room[index] != None) and (self.room[i] != None):
				if (self.room[index].intersects(self.room[i])):
					return True
			#Depends on the linear insertion into the room array object
			if(self.room[index] == None):
				return False
		return False

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
	for x in xrange(0, 8):
		map.RollRoom(x)
		map.addRoomToString(map.room[x])

	print map

	# Console 80 * 24