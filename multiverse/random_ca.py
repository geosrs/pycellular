# A totally random cellular automaton, where each cell's 1/0 state is
# determined randomly for each turn.

import sys, os.path, random
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import universe, perceiver

def transition(neighbors, state):
	return {'alive': random.randint(0,1)}

def color(state):
	return (255,255,255) if state['alive'] else (0,0,0)

def neighbors(x,y): return []

if __name__ == "__main__":
	initial = lambda: {'alive':0}
	u = universe.Universe(initial, transition, color, neighbors)
	p = perceiver.Perceiver(u)
	# u.add_hosts(['10.14.3.133', '10.14.3.134', '10.14.3.107'])
	p.perceive()
