from utils import *

class Grid: 

	__height = 0
	__width = 0

	cells ={}

	def elens(self,*args):
		return [len (filter(is_something,row)) for row in args]

	def __init__(self,*args):
		self.__height = len (args) if len(args)>0 else 10

		__width = [len (filter(is_something,row)) for row in args]

		self.__width =  max(__width) if len(__width) > 0 else 10
	
	def getwidth(self):
		return self.__width
	
	def getheight(self):
		return self.__height

	def writeCell(self, cell, position):
		self.cells[position] = cell

	def readCell(self,position):
		if position not in self.cells:
			return ""
		return self.cells[position]

