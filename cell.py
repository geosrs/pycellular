class Cell:

	def __init__(self,state={}):
		self.state = state
	
	def __str__(self): return self.__repr__()
	def __repr__(self): return str(self.state)
