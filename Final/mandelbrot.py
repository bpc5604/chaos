import matplotlib.pyplot as plt
import numpy as np

y=x=np.arange(-5,5,.005)

def function():		
	for i in x:
		for c in y:
			t=0	
			k=complex(i,c)
			z=0
			while t<100:
				z=z*z+k
				t+=1
			if abs(z)<1000000000:
				plt.plot(i,c,'b.-')
function()
plt.show()


