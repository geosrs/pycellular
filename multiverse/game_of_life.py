# The game of life cellular automata rules

import sys, os.path, random
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import universe, perceiver

black = (255,255,255)
white = (0,0,0)

def transition(neighbors, state):
	# 1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
	# 2. Any live cell with two or three live neighbours lives on to the next generation.
	# 3. Any live cell with more than three live neighbours dies, as if by overcrowding.
	# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
	neighbors_alive = len([x for x in neighbors.map(values) if x])
	if state['alive'] and (neighbors_alive < 2 or neighbors_alive > 3):
		return {'alive':False} # death
	elif not state['alive'] and neighbors_alive == 3:
		return {'alive': True} # birth
	else: return state

def color(state): return white if state['alive'] else black

def neighbors(x,y):
	return [
		(x,   y+1), # north
		(x+1, y+1), # northeast
		(x+1, y),   # east
		(x+1, y-1), # southeast
		(x,   y-1), # south
		(x-1, y-1), # southwest
		(x-1, y)    # west
	]

if __name__ == "__main__":
	initial = {'alive':0}
	u = universe.Universe(initial, transition, neighbors, color)
	p = perceiver.Perceiver(u)
	# u.add_hosts(['10.14.3.133', '10.14.3.134', '10.14.3.107'])
	p.perceive()
