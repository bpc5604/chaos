import matplotlib.pyplot as plt
import numpy as np

##define lorenz equations

def function():

	sigma=10
	b=8/3
	r=10
	t=0
	dt=.001
	x=y=z=0.001
	while t<5.0000:
		xdot=sigma*(y-x)
		ydot=r*x-y-x*z
		zdot=x*y-b*z
		
		x +=xdot*dt
		y +=ydot*dt
		z +=zdot*dt
		t += dt
		

		plt.plot(z,x,'b.-')

function()
plt.show()
