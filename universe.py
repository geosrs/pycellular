
# Run the cellular automata. This class only handles data, no visualization.
# Initialization, configuration, and control of your cellular automata universe.

import remote,time,cell

class Universe:

	def __init__(self,initial,transition,color,neighbors):
		"""
		Pass the initial state as a dict.

		Pass the transition function, which takes a list of neighbors and the
		cell's state, and returns the modified state

		Pass the color function which takes the cell's state and returns an rgba
		color quadruplet.
		"""
		self.initial = initial
		self.transition = transition
		self.color = color
		self.neighbors = neighbors

	def make_grid(self,rows,cols):
		self.grid = [[cell.Cell((x,y), self.initial()) for x in range(cols)] for y in range(rows)]
		# Initialize the neighbors for each cell
		for c in [c for row in self.grid for c in row]: # with numpy: for c in self.grid.flat
			for nx,ny in self.neighbors(c.x, c.y):
				c.neighbors.append(self.grid[ny % rows][nx % cols])
	
	def advance(self):
		"""
		Advance your cellular automata by 1 turn, updating the whole grid.
		"""
		for c in [c for row in self.grid for c in row]: # with numpy: for c in self.grid.flat
			c.state = self.transition(c.neighbors, c.state)
			c.color = self.color(c.state)

	def distribute(self):
		"""
		Distribute the universe to the network nodes
		"""
		pass
