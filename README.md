# Python cellular automata library

* Generalized
* Awesomized

Requirements: python 2.7, pyglet

## Run an example

  python multiverse/game_of_life.py

## Write your own cellular automata

### 1. Define the cell transition function

It takes a list of neighbor cells and the state of the cell as parameters, and
returns the cell's new state

Here is the transition function for the Game of Life, which first counts the
number of alive neighbors, and then applies the rules:

	def transition(neighbors, state):
		neighbors_alive = len([x for x in map(lambda n: n.state.values()[0], neighbors) if x])
		if state['alive'] and (neighbors_alive < 2 or neighbors_alive > 3):
			return {'alive':False} # death
		elif not state['alive'] and neighbors_alive == 3:
			return {'alive': True} # birth
		else:
			return state

### 2. Define the cell color function

This determines how the cell should look when visualized. The color function
takes the cell's state and returns an RGB triplet color value.

	def color(state):
		"White for alive, black for dead"
		return (255,255,255) if state['alive'] else (0,0,0)

### 3. Define the initial cell state

This beginning state makes each cell initially dead.

	initial = lambda: {'alive':0}

A random initial state:

	initial = labmda: {'alive': random.randint(0,1)}

### 4. Define your neighbor function

This function allows you to customize which other cells are the neighbors the
current cell cares about. It takes the x,y position of the current cell and
returns the x,y positions of all the neighbors you want access to inside the
transition funciton.

	def neighbors(x,y):
		return [
			(x,   y+1), # north
			(x+1, y+1), # northeast
			(x+1, y),   # east
			(x+1, y-1), # southeast
			(x,   y-1), # south
			(x-1, y-1), # southwest
			(x-1, y),   # west
			(x-1, y+1)  # northwest
		]

With these neighbors defined, the "neighbors" parameter in your transition
function will be initialized to the above 8 cell objects.

neighbors() can return anything; whatever works best for your transition
function. It may be a list of tuples or a dictionary if you want more data
annotation.

### 4. Initialize the cellular automata universe

Pass in the initial state function, the transition function, the color
function, and the neighbors function

	u = universe.Universe(initial, transition, color, neighbors)

### 5. Initialize the visualization of your automata (the "perceiver")

Pass the universe to the Perceiver constructor. You may optionally pass a cell size (in
pixels) and the dimensions of the grid (as a pair)

	p = Perceiver(u)

or:

	p = Perceiver(u, 20, (50,50))

for a 50x50 grid where each cell is 20 pixels.

If you do not pass the cell size or dimensions, they will be automatically
determined to fill your screen.

### 7. Start the event loop to watch your cellular automata:

	p.perceive()

### Todo
* Implement messages (and then langton's ant).
* Don't redraw the grid on every turn.
* Make the perceiver a texturegrid instead of a bunch of quads (I'm thinking instead of drawing a bunch of individual rectangles, we can use one large bitmap where each pixel is a square.)
* Cell fading effect (?).
* Implement more automata.
* GPU parallelization.
* More sophisticated data structure for the universe (?) -- quadtree (useful generally or only for GoL-similar CA's?).
