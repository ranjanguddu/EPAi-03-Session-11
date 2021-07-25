from Polygon import *

class Poly:
	def __init__(self, N):
		'''to instantiate the class'''

		print(f'Calling Poly __init__ ')
		self.max_vertices  = N
		self.Radius  = 15
		

	def __iter__(self):
		'''iter function within an iterable which return an iterator'''
		return self.PolyIterator(self.max_vertices, self.Radius)

	class PolyIterator:
		''' Iterator  class for Poly'''
		def __init__(self, vertices, rad):
			''' init funnction of Polygon Iterator '''
			self.vertices = vertices
			self.ctr = 3
			self.rad = rad

		def __iter__(self):
			'''iter function within an iterator which return self'''
			return self

		def __next__(self):
			'''__next__ need to  be defined for an iterator '''
			if self.ctr >= self.vertices+1:
				raise StopIteration

			else:
				poly = Polygon(self.ctr, self.rad)
				self.ctr += 1
				return poly

# p = Poly(5)
# # #print(list(p))

# p1 = iter(p)
# #print(p1)
# print(next(p1))
# print(next(p1))
# print(next(p1))
# print(next(p1))







