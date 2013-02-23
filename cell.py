class Cell:

	def __init__(self,loc,state={}):
		self.x, self.y = loc
		self.state = state
		self.neighbors = [] # a list of neighbor cells (accessible by the transition function)
	
	def __str__(self): return self.__repr__()
	def __repr__(self): return str(self.state)
