import numpy as np
import matplotlib.pyplot as plt


def function():

	n=1
	rm=5
	r=0
	i=0
	x=.03
	while r<.0005:
		r+= .001 
		#f1=x*np.exp(-r*(1-x))
		x=np.random.rand(1)
		while i<100:
			f=x*np.exp(-r*(1-x))
			x=f
			i+=.1
		while x<100:
			x+=1
			f=x*np.exp(-r*(1-x))
			x=f
			plt.plot(r,x,'--bo')
			
	plt.show()
function()
