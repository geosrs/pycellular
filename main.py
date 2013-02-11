
import sys,universe,perceiver

if __name__ == "__main__":
	u = universe.Universe()
	p = perceiver.Perceiver(universe.Universe())
	u.add_hosts(['10.14.3.133', '10.14.3.134', '10.14.3.107'])
	p.perceive()
