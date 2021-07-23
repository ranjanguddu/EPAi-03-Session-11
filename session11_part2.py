from session11 import *

class PolygonIter:
	def __init__(self, N):
		'''to instantiate the class'''

		print(f'Calling PolygonIter __init__ ')
		if isinstance(N, int):
			if N<3:
				raise IndexError('Minimum 3 vertices Polygon is possible')
			else:
		
				self.max_vertices  = N
				self.Radius  = 15
		else:
			raise TypeError('For a Ploygon, no of Vertices has to be a number')
		

		

	def __len__(self):
		'''find the length of this sequence type'''
		print(f'Calling PolygonIter __len__ ')
		return self.max_vertices-2

	def __getitem__(self,i):
		'''this method actually makes this class sequence type'''
		print(f'Calling PolygonIter __getitem__ ')
		if isinstance(i, int):
			if i<0 or i >= self.max_vertices-2:
				raise IndexError('passed index is out of range')
			else:
				return Polygon(3+i, self.Radius)
		elif isinstance(i,slice):
			start,stop,step = i.indices(self.max_vertices-2)
			
			rng = range(start,stop,step)
			return [Polygon(3+index, self.Radius) for index in rng]
		else:
			raise TypeError('Index has to be an integer')

	def max_eff_polygon(self):
		''' method to find the polygon having maximum area/perimiter ratio'''
		max_ratio = 0
		for i in range(3, self.max_vertices+1):
			poly = Polygon(i, self.Radius)
			
			ratio = float(poly.area())/float(poly.perimiter())
			#print(f'{i}:{ratio}')
			if ratio > max_ratio:
				max_side = i
				max_ratio = ratio

		return f'For circumradiud {self.Radius},Polygon having {max_side} vertices is max efficiency polygon'




	def __repr__(self):
		'''user helping method to know about the object '''
		print(f'Calling PolygonIter __repr__ ')
		return f'polygon sequencer is created having  maximum no of vertices is {self.max_vertices}'

	def __iter__(self):
		print(f'Calling PolygonIter __iter__ ')
		return self.PolygonIterator(self)

	class PolygonIterator:

		def __init__(self, poly_obj):
			print(f'Calling PolygonIterator __init__ ')
			self._poly_obj = poly_obj
			self._index = 0

		def __iter__(self):
			print(f'Calling PolygonIterator __iter__ ')
			return self

		def __next__(self):
			print(f'Calling PolygonIterator __next__ ')
			#print(f'In __next__ having self._index  = {self._index}')
			if self._index >= self._poly_obj.max_vertices - 2:
				raise StopIteration
			else:
				item = Polygon(3+self._index, self._poly_obj.Radius)
				self._index = self._index + 1
				print(f'here: {self._index}')
				return item

p = PolygonIter(8)
#print(next(iter(p)))

for item in p:
	print(item)



