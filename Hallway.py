class Hallway(object):
	def __init__(self,  sideA, sideB, room_indices=[], hallway_indices=[], char = ' '):
		#sideA will always be the leftmost or the uppermost.
		#enforce alignment
		
		self.associatedRoomss = room_indices
		self.associatedHallways = hallway_indices
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
				print "Unable to work with a hallway setup"
				raise Exception('Hallway','Hallways can only be a line')