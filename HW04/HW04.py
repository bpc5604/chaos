
import matplotlib.pyplot as plt
import numpy as np

def integrate(x,y):
	t=0
	dt=.01
	while t<1:
		dxdt=y           #x dot function
		dydt=-2*x-3*y    #y dot function
		x+=dxdt*dt
		y+=dydt*dt
		t+=dt

		plt.plot(t,x,'b.-')
		plt.plot(t,y,'r.-')
	
z=np.arange(-1,1)
d=np.arange(-1,1)
for i in range(-1,1):
	integrate(i,.001)
	integrate(i,.01)
	integrate(i,50)
	integrate(i,-50)

b=np.linspace(0,1.2)        #defines range of x values for quiver plot
c=np.linspace(-100,150)     #defines range of y values for quiver plot
integrate(100,1)
integrate(-100,1)
W,Z=np.meshgrid(b,c)       
xdot=Z			#xdot function
ydot=-2*W-3*Z		#ydot function


plt.quiver(W,Z,xdot,ydot,color='Black',units='xy')

plt.show()

