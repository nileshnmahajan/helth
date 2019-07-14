import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

def multi_line():
	t1 = np.arange(0.0, 1.0, 0.01)
	for n in [1, 2, 3, 4]:
		ax.plot([1, 2, 3, 4], t1**n, label="n=%d"%(n,))
	ax.legend()
	fig.savefig('graphs/static/multi.png')
	
	
	#plt.show()
#multi_line()	