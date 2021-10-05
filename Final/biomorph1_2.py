import matplotlib.pyplot as plt
import numpy as np



y=x=np.arange(-1.50,1.50,.02)
def function():
		
	for i in x:
		for c in y:
			t=0
			k=complex(0.5,0)
			z=complex(i,c)
			while t<10:
				z=z*z*z+k
				t+=1
			if abs(z)>100:
				plt.plot(i,c,'b.-')
function()
plt.show()


