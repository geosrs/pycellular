# Python cellular automata library

* Generalized
* Parallelized
* Awesomized

### 1. Define the cell transition function

It takes a list of neighbor cells and the state of the cell as parameters, and
returns the cell's new state

	def transition(neighbors, state):
		"Random cell transition"
		return {'alive': random.randint(0,1)}

### 2. Define the cell color function

This determines how the cell should look when visualized. The color function
takes the cell's state and returns an RGB triplet color value.

	def color(state):
		"White for alive, black for dead"
		return (255,255,255) if state['alive'] else (0,0,0)

### 3. Define the initial cell state

The beginning state on turn 0 of every cell.

	initial = {'alive':0}

### 4. Initialize the cellular automata universe

Pass in the initial state, the transition function, and the color function

	u = universe.Universe(initial, transition, color)

### 5. Initialize the visualization of your CA (the "perceiver")

Pass the universe to the constructor. You may optionally pass a cell size (in
pixels) and the dimensions of the grid (as a pair)

	p = Perceiver(u)

or:

	p = Perceiver(u, 20, (50,50))

for a 50x50 grid where each cell is 20 pixels.

If you do not pass the cell size or dimensions, they will be automatically
determined to fill your screen.

### 6. Add a list of hostnames for paralellization:

	u.add_hosts(['10.14.3.133', '10.14.3.134', '10.14.3.107'])

### 7. Start the event loop to watch your cellular automata:

	p.perceive()

#### Runs on:
python2.x

#### Dependencies:
execnet
piglet

### Todo
* Benchmarking.
* Pass grid of initial states.
