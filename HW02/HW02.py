#written using python2.7 (renamed .py to .txt)


#created 2 plots (1 semilog,1 linear)

import numpy as np

import matplotlib.pyplot as plt
time=np.linespace(-3,3)
def integrate(r,k):
	t=0
	dx=.001   #small perturbation
	x=.99  #initial x
	dt=.001
	while t<1:
		dxdt=np.sin(time)-np.sin(theta)   #function
		x+= dxdt*dt     #incrimenting x values
		t+=dt           #incrimenting time values
		plt.plot(t,x,'--bo')
		plt.ylabel("X(t)")
		plt.xlabel("Time")
		#plt.semilogy(t,x,'--bo')
	#print(t,x)
integrate(time, theta)



#integrate(40,3)   ##r affects rise rate, k leads to asymptote 
#integrate(20,2)
#integrate(10,4)   
#integrate(15,1)
#integrate(2,300)
plt.show()


