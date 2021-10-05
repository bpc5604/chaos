import numpy as np
import matplotlib.pyplot as plt

##lorentz equations
def function():
    sigma = 10   ##Prandtl number
    r = 126.52    ##Rayleigh number
    b = 8/3
    z=y=x=.00001

    t = 0
    dt=.001
    while t < 10.0000:
        xdot = sigma*(y-x)
        ydot = r*x-y-x*z
        zdot = x*y-b*z
        x += xdot*dt
        y += ydot*dt
        z += zdot*dt
        t+= dt
        plt.subplot(1,3,1)
        plt.plot(t,x,'.b-')
	plt.title('x(t)')
        plt.subplot(1,3,2)
        plt.plot(t,y,'b.-')
	plt.title('y(t)')
        plt.subplot(1,3,3)
        plt.plot(z,x,'b.-')
	plt.title('Z(x)')



#plt.xlim(5,100)
function()
plt.title('R=126.52')
#plt.legend()
plt.show()
