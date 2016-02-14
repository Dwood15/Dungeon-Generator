class Hallway(object):
	def __init__(self,  sideA, sideB, room_indices=[], hallway_indices=[], char = ' '):
		#sideA will always be the far left or the topmost.
		#enforce alignment
		self.associatedRoomIndexes = room_indices
		self.associatedHallIndexes = hallway_indices
		self.character = char
		
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