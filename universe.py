# Initialization, configuration, and control of your cellular automata u/niverse.

import execnet,sys,os,socket,remote,matplotlib

class Universe:

	def __init__(self, dimensions):
		"""
		Dimensions are passed as a list of Int. Each entry is the length of that dimension.
		For example: [3,3,3] is a 3d world with dimensions 3x3x3
		"""
		# - Initialize the data structure and all the nodes.
		# - Initialize execnet
		# ...
		# Initialize the data structure
		# Initialize execnet
		self.hosts = set(['localhost'])
		self.gws = [execnet.makegateway("ssh=localhost")]
		cs = [gw.remote_exec(remote) for gw in self.gws]
		results = [c.receive() for c in cs]
		print(results)

	def set_state(universe):
		

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

