import math

class Polygon:
	'''this  is a polygon iterable class which takes radis and side leangth 
	2 parametersa and calculate few parameters on Polygon'''

	def __init__(self, n, r):
		print(f'Calling Polygon __init__ ')
		'''to instantiate the class'''

		if isinstance(n, int) and isinstance(r, int):
			if n<3:
				raise IndexError('Minimum 3 vertices Polygon is possible')
			else:
		
				self.num_side = n
				self.radius = r
		else:
			raise TypeError('For a Ploygon, no of Vertices &  Radius has to be a number')

	def edges(self):
		'''return no of edges '''
		return self.num_side

	def vertices(self):
		'''return no of vertices '''
		return self.num_side

	def interior_anagle(self):
		'''calculate interior angle '''
		return f'{(self.num_side-2)*180/self.num_side:.1f}'

	def edge_length(self):
		'''calculate edge length '''
		return f'{2*self.radius*math.sin(math.pi/self.num_side):.2f}'

	def apothem(self):
		'''calculate apothem '''
		return f'{self.radius*math.cos(math.pi/self.num_side):.2f}'

	def area(self):
		'''calculate area '''
		return f'{0.5*self.num_side*float(self.apothem())*float(self.edge_length()):.2f}'
	
	def perimiter(self):
		'''calculate perimiter '''
		return f'{self.num_side*float(self.edge_length()):.2f}'

	def __eq__(self,other):
		''' implementing this method to copmare 2 polygomn  object'''
		if isinstance(other, Polygon):
			return self.num_side == other.num_side and self.radius == other.radius

		else:
			return "Can't compare different kind of object"
	
	def __gt__(self,other):
		'''to find if one polygon vertices no is greater than other or not'''
		if isinstance(other, Polygon):
			return self.num_side>other.num_side
			



	def __repr__(self):
		'''__rper__ method to give user an idea about the object creation'''
		print(f'Calling Polygon __repr__ ')
		return f'Polygon having {self.num_side} sides and circumradius {self.radius} units is created\n'


