import matplotlib.pyplot as plt
import numpy as np

#k=complex(0.5,0)

y=x=np.arange(-1.5,1.5,.01)
"""
def z(x,iy):
	zn=(x+iy)**3 + 0.05
	zmag=
	if zmag>100
		list.append()
	plt.plot(list)
"""
def function():
	
		
	for i in x:
		for c in y:
			t=0
			k=complex(0.5,0)
			z=complex(i,c)
			while t<15:
				z=z*z*z+k
				t+=1
			if abs(z)>15 or z.real>3.9 or abs(z.imag)<3.9:
				plt.plot(i,c,'b.-')
	#			break
function()
plt.show()


