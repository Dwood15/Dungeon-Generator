class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __eq__(self, rhs):
		return self.x == rhs.x and self.y == rhs.y
	
	def isVerticallyAligned(self, rhs):
		return self.x == rhs.x
		
	def isHorizontallyAligned(self, rhs):
		return self.y == rhs.y
		
#A utility class for describing the range of sizes of rooms
class DimRange(object):
	def __init__(self, x1, x2, y1, y2):
		self.min = Point(x1, y1)
		self.max = Point(y1, y2)