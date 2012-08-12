import unittest

from model.Grid import Grid
from model.utils import *

	
class ConversionTest(unittest.TestCase):

	def test_row_from_array(self):
		row = ["1","2","3"]
		self.assertEqual("1&2&3\\",to_latex_row(row))

	def test_with_empty_cell(self):
		row = ["1","","3"];
		self.assertEqual("1&&3\\",to_latex_row(row))


class GridTest(unittest.TestCase):

	def test_writing_a_cell_should_not_modify_others(self):
		grid = Grid()	

		grid.writeCell("hello",(0,0))	
		self.assertEqual("hello",grid.readCell((0,0)))

		grid.writeCell("good bye",(0,0))
		self.assertEqual("good bye",grid.readCell((0,0)))
		
		grid.writeCell("In a new cell",(0,1))
		self.assertEqual("good bye",grid.readCell((0,0)))
		self.assertEqual("In a new cell",grid.readCell((0,1)))


	def test_read_empty_cell_should_return_empty_string(self):
		grid = Grid()
		self.assertEqual("",grid.readCell((0,0)))




if __name__=="__main__":
	unittest.main()
