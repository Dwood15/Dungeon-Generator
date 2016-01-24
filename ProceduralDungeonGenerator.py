#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random
from Room import *

NUMBERROOM = 8

class Map(object):
    """docstring for Map"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._map = ["#" for i in xrange(0, width * height)]
        self.room = [None] * NUMBERROOM

    def __str__(self):
        return "\n".join(["".join(self._map[start:start + self.width]) for start in xrange(0, self.height * self.width, self.width)])

    def addRoom(self, room):
        for i in [(x + y * self.width) for x in xrange(room.left, room.left + room.height) for y in xrange(room.top, room.top + room.height)]:
            self._map[i] = " "

    # def hallway(self, room1, room2, width):

if __name__ == '__main__':
    map = Map(80, 24)

    for x in xrange(0, NUMBERROOM):
        map.room[x] = Room(map.height, map.width)
        map.addRoom(map.room[x])

    print map

    # Console 80 * 24