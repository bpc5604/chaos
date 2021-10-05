import matplotlib.pyplot as plt
import math as m
import numpy as np
#defines integration function, takes another function and limits
#as input, predefined stepsize
def integral(f,a,b,dx=.01):
	i=a
	s=0
	b=2
	while i<=b:
		s+=f(i)*dx
		i+=dx
	return s
def function(x):
	return 1-x**2

for i in range (0,5):
 print(integral(function,0,i))

t=np.linspace(1,10,100)

y=np.exp(2*t)
plt.semilogx(y,t)
plt.show()
plt.plot(y,t)
plt.show()

