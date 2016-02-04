#!/usr/bin/env python
# -*-coding:Utf-8 -*

import random
from Room import *

NUMBERROOM = 8

class Map(object):
    """docstring for Map"""
    # def __init__(self, width, height):
    #     self.width = width
    #     self.height = height
    #     self._map = [["#" for x in xrange(self.width)] for y in xrange(self.height)] 
    #     self.room = [None] * NUMBERROOM

    # def __str__(self):
    #     strMap = ""
    #     for y in xrange(self.height):
    #         for x in xrange(self.width):
    #             strMap += self._map[y][x]
    #         strMap += "\n"
    #     return strMap

    # def addRoom(self, room):
    #     if self._map[room.top][room.left] != "#":
    #         return None

    #     self._map[room.top][room.left] = " "
    #     currentWidth = 1
    #     currentHeight = 1
    #     while currentHeight < 4:
    #         if self.growBottom(room, currentHeight, currentWidth):
    #             currentHeight += 1
    #         else:
    #             return None

    #     while currentWidth < 4:
    #         if self.growRight(room, currentHeight, currentWidth):
    #             currentWidth += 1
    #         else:
    #             return None

    #     stopRight = None
    #     stopBottom = None
    #     while not stopRight and not stopBottom:
    #         if currentWidth < room.width and not stopRight:
    #             if self.growRight(room, currentHeight, currentWidth): 
    #                 currentWidth += 1
    #             else:
    #                 stopRight = True
    #                 room.width = currentWidth

    #         if currentHeight < room.height and not stopBottom:
    #             if self.growBottom(room, currentHeight, currentWidth): 
    #                 currentHeight += 1
    #             else:
    #                 stopRight = True
    #                 room.height = currentHeight

    #     return room

    # def growRight(self, room, currentHeight, currentWidth):
    #     for x in xrange(1,9):
    #         if currentHeight >= x:
    #             if self._map[room.top + currentHeight - x][room.left + currentWidth] == "#":
    #                 self._map[room.top + currentHeight - x][room.left + currentWidth] = " "
    #             else:
    #                 return False
    #     return True

    # def growBottom(self, room, currentHeight, currentWidth):
    #     for x in xrange(1,9):
    #         if currentWidth >= x:
    #             if self._map[room.top + currentHeight][room.left + currentWidth - x] == "#":
    #                 self._map[room.top + currentHeight][room.left + currentWidth - x] = " "
    #             else:
    #                 return False
    #     return True

    # def hallway(self, room1, room2, width):

    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._map = ["#" for i in xrange(0, width * height)]
        # self._map = [["#" for x in xrange(self.width)] for y in xrange(self.height)] 
        self.room = [None] * NUMBERROOM

    # def addRoom(self, top, left, height, width):
    #     for i in [(x + y * self.width) for x in xrange(left, left + width) for y in xrange(top, top + height)]:
    #         self._map[i] = " "

    def addRoom(self, room):
        for i in [(x + y * self.width) for x in xrange(room.left, room.left + room.width) for y in xrange(room.top, room.top + room.height)]:
            self._map[i] = " "

    # def addRoom(self, room):
    #     if self[room.left, room.top] != "#":
    #         return None

    #     self[room.left, room.top] = "*"
    #     currentWidth = 1
    #     currentHeight = 1
    #     while currentHeight < 6:
    #         if self.growBottom(room, currentHeight, currentWidth):
    #             currentHeight += 1
    #         else:
    #             return None

    #     while currentWidth < 6:
    #         if self.growRight(room, currentHeight, currentWidth):
    #             currentWidth += 1
    #         else:
    #             return None

    #     stopRight = None
    #     stopBottom = None
    #     while not stopRight and not stopBottom:
    #         if currentWidth < room.width and not stopRight:
    #             if self.growRight(room, currentHeight, currentWidth): 
    #                 currentWidth += 1
    #             else:
    #                 stopRight = True
    #                 room.width = currentWidth

    #         if currentHeight < room.height and not stopBottom:
    #             if self.growBottom(room, currentHeight, currentWidth): 
    #                 currentHeight += 1
    #             else:
    #                 stopRight = True
    #                 room.height = currentHeight

    #     return room

    def growRight(self, room, currentHeight, currentWidth):
        for x in xrange(1, currentHeight):
            if currentWidth >= 2:
                if x == 1 or x == currentHeight:
                    if self[room.left + currentWidth, room.top + currentHeight - x] == "#":
                        self[room.left + currentWidth, room.top + currentHeight - x] = "*"
                    else:
                        return False
                else:
                    if self[room.left + currentWidth, room.top + currentHeight - x] == "#":
                        self[room.left + currentWidth - 1, room.top + currentHeight - x] = " "
                        self[room.left + currentWidth, room.top + currentHeight - x] = "*"
                    else:
                        return False
        return True

    def growBottom(self, room, currentHeight, currentWidth):
        for x in xrange(1, currentWidth):
            if currentHeight >= 2:
                if x == 1 or x == currentWidth:
                    if self[room.left + currentWidth - x, room.top + currentHeight] == "#":
                        self[room.left + currentWidth - x, room.top + currentHeight] = "*"
                    else:
                        return False
                else:
                    if self[room.left + currentWidth - x, room.top + currentHeight] == "#":
                        self[room.left + currentWidth - x - 1, room.top + currentHeight] = " "
                        self[room.left + currentWidth - x, room.top + currentHeight] = "*"
                    else:
                        return False
        return True

    def __str__(self):
        return "\n".join(["".join(self._map[start:start + self.width]) \
                for start in xrange(0, self.height * self.width, self.width)])

    def __getitem__(self, i):
        x, y = i
        return self._map[x + y * self.width]

    def __setitem__(self, i, val):
        x, y = i
        self._map[x + y * self.width] = val

if __name__ == '__main__':
    map = Map(80, 24)

    for x in xrange(0, NUMBERROOM):
        # width = random.randrange(4, 8)
        # height = random.randrange(4, 8)
        # left = random.randrange(1, map.width - width)
        # top = random.randrange(1, map.height - height)
        # map.addRoom(top, left, height, width)

        map.room[x] = Room(map.height, map.width)
        map.addRoom(map.room[x])

    print map

    # Console 80 * 24

    # self._map = ["#" for i in xrange(0, width * height)]

    # return "\n".join(["".join(self._map[start:start + self.width]) for start in xrange(0, self.height * self.width, self.width)])

    #     for i in [(x + y * self.width) for x in xrange(room.left, room.left + room.height) for y in xrange(room.top, room.top + room.height)]:
    #         self._map[i] = " "
'''
for s in range(0,80,5):
    for t in range(0,24,5):
        print "#" + 0.6215*t-11.362*s**0.16+0.396*t*s**0.16, '\t',
    print
'''