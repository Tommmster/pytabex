from model.Grid import Grid

class Controller:
	grid = None

	def __init__(self, theGrid):
		self.grid = theGrid	
			
	def getTopText(self):
		position = self.grid.getCurrent()
		return self.grid.readCell(position)
	

	def clickAt(self, position):
		self.grid.moveTo(position)		

	def writeTopText(self, text):
		position = self.grid.getCurrent()
		self.grid.writeCell(text,position)
	
	def getCurrentCellContent(self):
		return self.grid.readCell(self.grid.getCurrent())


