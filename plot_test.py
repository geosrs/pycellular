import matplotlib as mpl
mpl.use('WXAgg')

import matplotlib.pyplot as pp
import matplotlib.pylab as pl
import matplotlib.image as mpimg
import time

# plot config
pp.close('all')
pp.ion()

def animate_for(steps, wait, *args):
	fig = pp.figure(figsize=(1024,768), dpi=1)
	ax = fig.add_subplot(111)
# Kewl grid sizes:
# 768,1024
# 384,512
# 192,256
# 96,128
# 48,64
# 24,32
# 12,16
	x,y = 96,128
	img = ax.imshow(pl.rand(x,y), interpolation="nearest")
	img.axes.get_xaxis().set_visible(False)
	img.axes.get_yaxis().set_visible(False)
	pp.tight_layout(pad=0, w_pad=0, h_pad=0)
	fig.canvas.draw()
	for i in range(steps):
		img.set_array(pl.rand(x,y))
		fig.canvas.draw()
		time.sleep(wait)

if __name__ == '__main__':
	import sys
	if sys.argv[1] is None or sys.argv[2] is None:
		print('usage: \n python plot_test.py [step_amount] [step_interval_seconds]')
	else: animate_for(int(sys.argv[1]), float(sys.argv[2]))
