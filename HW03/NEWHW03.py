#written using python2.7 

import matplotlib.pyplot as plt
import numpy as np

#[r]= 1/time
#[k]= people


def integrate(x,y):
	t=0 
	dt=.001
	while t<1:
	
		dxdt=x+np.exp(-y)    #function   #xdot
		x+= dxdt*dt

		dydt=-y   #ydot
		y+=dydt*dt  
		
		t+=dt                #incrementing time values
		
		#plt.ylabel("X(t),Y(t)")
		#plt.xlabel("Time")


		plt.plot(t,x,'bo-')
		plt.plot(t,y,'ro-') 
		
#integrate(1,-1)
b=np.linspace(-3,3)
c=np.linspace(-2,2)

W,Z=np.meshgrid(b,c)
xdot=-4*W+6*Z
ydot=-3*W+3*Z
plt.axis(option='on')


plt.streamplot(W,Z,xdot,ydot, density=3)	
plt.show()


