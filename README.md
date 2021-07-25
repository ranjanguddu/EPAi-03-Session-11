# Session-11 
## Topic:
* ### List Comprehension
* ### Iterators
* ### Iterable
___
## 1. List Comprehension
List comprehensions is a method to create new lists from other iterables like tuples, strings, arrays, lists, etc.

A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element. 

Syntax: 
```python
newList = [ expression(element) for element in oldList if condition ]
```

Example 1.

Lets see a below program to create list of squares of number:

```python
square =[]
for i in range(1,10):
    square.append(i**2)
print(square)
```
```
Output:
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```
We can do the same thing using List Comprehension:

```python
squares = [i**2 for i in range(1,10)]
print(squares)
```
We can also put condition  while writing List Comprehension:
```python
squares = [i**2 for i in range(1,10) if i%2 == 0]
print(squares)
```

Example 2.

Let's take another example of List Comprehension of nnested loop:

```python
table = []

for i in range(1,11):
    row =[]
    for j in range(1,11):
        row.append(i*j)
    table.append(row)

print(table)
```
List comprehension version of the above program is:
```python
table  = [[i*j for j in range (1,11)] for i in range(1,11)]
```

## 2. Iterators
Iterators are the python object which returns itself. For iterators we need to implement below 2 methods:

* __ iter__ : method that is called for the initialization of an iterator. This returns an iterator object

* __ next__: The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object which further uses next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.

Example:
```python
s  = 'Vikash'
s_iter = iter(s)
while True:
    try:
        item = next(s_iter)
        print(item)
    except StopIteration:
        break
```
```
Output:
V
i
k
a
s
h
```

## 3. Iterables
An iterable is any Python object capable of returning iterators.  To make a class as iterable, you have to implement the __iter__() and __next__() methods in that class. 

The __iter__() method allows us to make operations on the items or initializing the items and returns an iterator object.

The __next__() method allows us to do operations and it should return the next value of the sequence.

Example:
```python

from datetime import timedelta, date

class DateIterable:

    def __init__(self, start_date, end_date):
        # initilizing the start and end dates
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        #returning __iter__ object
        return self

    def __next__(self):
        #comparing present_day with end_date,
        #if present_day greater then end_date stoping the iteration
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


if __name__ == '__main__':
    for day in DateIterable(date(2020, 1, 1), date(2020, 1, 6)):
        print(day)

```
```
output:

2020-01-02
2020-01-03
2020-01-04
2020-01-05
```

## Important points related to Iterators and Iterables:
__ iter __ function of iterators returnn itself where as in iterable it returnns an iterator

Q. Is list iterable or iterator in python?<br>
A. List is **iterable** as it doesn't get exhausted.

Q. range() in python  is iterable or iterators?<br>
A. **iterable**

Field | Iterators | Iterables
---------|----------|---------
 __ iter__ | yes | Yes
 __ next __| Yes | may/may not
 __ getitem __ | may/may not | may/may not

If we want to make the object subscribable,  then we implement __ getitem __ method.

### Assignment:
####  Refactor the [Ploygon(sequence)](https://github.com/ranjanguddu/EPAi-03_session-10) type into an iterable.

```python
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

```
**Session - 11 Assignment iPython NoteBook can be foud [here](https://github.com/ranjanguddu/EPAi-03-Session-11/blob/main/Session-11_output.ipynb)**






