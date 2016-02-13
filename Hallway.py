class Hallway(object):
	def __init__(self,  sideA, sideB, associated_room_indices=[], associated_hallways=[], char = ' '):
		#sideA will always be the far left or the topmost.
		#enforce alignment
		self.associatedRoomIndexes = associated_room_indices
		self.associatedHallIndexes = associated_hallways
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