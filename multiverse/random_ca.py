# A totally random cellular automaton, where each cell's 1/0 state is
# determined randomly for each turn.

import sys, os.path, random
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import universe, perceiver

def transition(neighbors, state):
	return {'alive': random.randint(0,1)}

def color(state):
	if state['alive']: return (255,255,255)
	else:              return (0,0,0)

if __name__ == "__main__":
	initial = {'alive':0}
	u = universe.Universe(initial, transition, color)
	p = perceiver.Perceiver(u)
	u.add_hosts(['10.14.3.133', '10.14.3.134', '10.14.3.107'])
	p.perceive()
