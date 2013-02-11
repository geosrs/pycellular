
# Run the cellular automata. This class only handles data, no visualization.
# Initialization, configuration, and control of your cellular automata universe.

import execnet,remote,time,cell

class Universe:

	def __init__(self,initial,transition,color):
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
		# Initialize execnet
		self.hosts = set(['localhost'])
		self.gws = [execnet.makegateway("ssh=localhost")]
		cs = [gw.remote_exec(remote) for gw in self.gws]
		results = [c.receive() for c in cs]
		print(results)
		# Initialize data
		# self.square = pyglet.image.SolidColorImagePattern(color=(255,255,255,255)).create_image(self.cell_size,self.cell_size)

	def make_grid(self,rows,cols):
		self.grid = [[cell.Cell(self.initial) for c in range(cols)] for r in range(rows)]
	
	def advance(self):
		"""
		Advance your cellular automata by 1 turn, updating the whole grid.
		"""
		for x in range(len(self.grid)):
			row = self.grid[x]
			for y in range(len(row)):
				self.grid[x][y].state = self.transition([],self.grid[x][y].state)
				self.grid[x][y].color = self.color(self.grid[x][y].state)

	def add_hosts(self,hosts):
		"""
		Pass hosts as a list of strings
		"""
		self.hosts = self.hosts.union(hosts)
		self.gws = [execnet.makegateway("ssh=" + host) for host in self.hosts]
		cs = [gw.remote_exec(remote) for gw in self.gws]
		results = [c.receive() for c in cs]
		print(results)

	def distribute(self):
		"""
		Distribute the universe to the network nodes
		"""
		pass
