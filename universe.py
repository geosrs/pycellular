
# Run the cellular automata. This class only handles data, no visualization.
# Initialization, configuration, and control of your cellular automata universe.

import execnet,remote,time,cell

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
		self.neighbors = color
		# Initialize execnet
		self.hosts = set(['localhost'])
		self.gws = [execnet.makegateway("ssh=localhost")]
		cs = [gw.remote_exec(remote) for gw in self.gws]
		results = [c.receive() for c in cs]
		print(results)

	def make_grid(self,rows,cols):
		self.grid = [[cell.Cell((x,y), self.initial) for x in range(cols)] for y in range(rows)]
		# Initialize the neighbors for each cell
		for cell in self.grid.transpose():
			for nx,ny in self.neighbors(cell.x, cell.y):
				cell.neighbors.append(self.grid[ny % rows][nx % cols])
	
	def advance(self):
		"""
		Advance your cellular automata by 1 turn, updating the whole grid.
		"""
		for y in range(len(self.grid)):
			row = self.grid[y]
			for x in range(len(row)):
				self.grid[y][x].state = self.transition([],self.grid[x][y].state)
				self.grid[y][x].color = self.color(self.grid[x][y].state)

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
