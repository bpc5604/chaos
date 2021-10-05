
import matplotlib.pyplot as plt
import numpy as np
a=0
def integrate(x,y):
	t=0
	dt=.1
	while t<1:
		dxdt=a+x**2-x*y
		dydt=y**2-x**2-1
		x+=dxdt*dt
		y+=dydt*dt
		t+=dt

		plt.plot(t,x,'b.-')
		plt.plot(t,y,'r.-')
	
z=np.arange(-1,1)
d=np.arange(-1,1)
"""for i in range(-1,1):
	integrate(i,.001)
	integrate(i,.01)
	integrate(i,1)
	integrate(i,-.1)
"""
integrate(-5,5)
b=np.linspace(-5,5)
c=np.linspace(-40,80)

W,Z=np.meshgrid(b,c)
xdot=a+W**2-W*Z
ydot=Z**2-W**2-1


plt.quiver(W,Z,xdot,ydot,color='Black',units='xy')

plt.show()

