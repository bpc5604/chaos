#written using python2.7 (renamed .py to .txt)


#created 2 plots (1 semilog,1 linear)
#I decreased step size and increased time to get a longer plot

import matplotlib.pyplot as plt

def integrate(r,k):
	t=0 
	dx=.001   #small perturbation
	x=0.001  #initial x
	dt=.01
	while t<12:
		dxdt=r*x*(1-x/k)/(k*r)   #function
		x+= dxdt*dt/k   #incrimenting x values
		t+=dt*r           #incrimenting time values
		#plt.plot(t,x,'--bo')
		plt.ylabel("X(t)")
		plt.xlabel("Time")
		plt.semilogy(t,x,'--bo')
	#print(t,x)
integrate(4,30)   ##r affects rise rate, k leads to asymptote 
integrate(2,2)
integrate(1,4)   
integrate(15,1)
integrate(20,5)
plt.show()


