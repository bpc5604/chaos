
import matplotlib.pyplot as plt
import numpy as np

def integrate(x,y):
	t=0
	dt=.01
	while t<1:
		dxdt=5*x+10*y
		dydt=-x-y
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
	integrate(i,1)
	integrate(i,-.1)

b=np.linspace(0,1.2)
c=np.linspace(-40,80)

W,Z=np.meshgrid(b,c)
xdot=5*W+10*Z
ydot=-1*W-1*Z


plt.quiver(W,Z,xdot,ydot,color='Black',units='xy')

plt.show()

