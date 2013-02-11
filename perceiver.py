# Visualize the universe.

import pyglet
from pyglet import window
from pyglet import clock
from pyglet import font

class Perceiver(pyglet.window.Window):

	def __init__(self, universe, cell_size=None, dimensions=None):
		"""
		Visualization is 2d only for now.

		Pass cell size in pixels, dimensions of the grid (as a pair), and the
		universe object.

		Leave dimensions and cell_size blank if you want the grid to fill the screen.
		"""
		self.universe = universe
		# Initialize the pyglet window at fullscreen
		window.Window.__init__(self,fullscreen=True)
		# Detect screen height and width.
		platform = pyglet.window.get_platform()
		display = platform.get_default_display()
		screen = display.get_default_screen()
		self.screen_width = screen.width
		self.screen_height = screen.height
		# Initialize the number of columns and rows
		self.cell_size = cell_size
		if dimensions is None:
			if cell_size is None:
				self.cell_size = 10
			self.rows = self.screen_height / self.cell_size
			self.cols = self.screen_width / self.cell_size
		else:
			self.rows, self.cols = dimensions
			if cell_size is None:
				self.cell_size = self.screen_height / self.rows
		universe.make_grid(self.rows,self.cols)
		print 'cell size: %d' % self.cell_size
		print 'columns: %d' % self.cols
		print 'rows: %d' % self.rows

	def perceive(self):
		"""
		Despite the impliciation in the method definition, it's not actually
		perceiving itself, as cool as that sounds.
		"""
		# Start the piglet event loop.
		pyglet.clock.schedule(self.gl_draw)
		pyglet.app.run()

	def gl_draw(self,dt):
		self.clear()
		self.universe.advance()
		self.gl_draw_cells()
		self.gl_draw_grid()

	def gl_draw_cell(self,row,col,rgb):
		pyglet.gl.glColor3ub(*rgb)
		x1,y1 = col*self.cell_size, row*self.cell_size
		x2,y2 = col*self.cell_size+self.cell_size, row* self.cell_size + self.cell_size
		pyglet.gl.glVertex2f(x1,y1)
		pyglet.gl.glVertex2f(x1,y2)
		pyglet.gl.glVertex2f(x2,y2)
		pyglet.gl.glVertex2f(x2,y1)
		return self

	def gl_draw_grid(self):
		# Horizontal lines and squares
		pyglet.gl.glColor3f(0.23,0.23,0.23)
		for row in range(self.rows):
			pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
				('v2i', (0, row * self.cell_size, self.cell_size * self.cols, row * self.cell_size)))
		# Vertical lines
		for col in range(self.cols):
			pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
					('v2i', (col * self.cell_size, 0, col * self.cell_size, self.cell_size * self.rows)))

	def gl_draw_cells(self):
		# Below two lines may be useful for fading animation. Not sure.
		# pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
		# pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
		pyglet.gl.glBegin(pyglet.gl.GL_QUADS)
		for x in range(len(self.universe.grid)):
			row = self.universe.grid[x]
			for y in range(len(row)): self.gl_draw_cell(x,y, row[y].color)
		pyglet.gl.glEnd()
