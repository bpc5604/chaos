import numpy as np
import matplotlib.pyplot as plt

## fixed initial value of r
r=3.8495
##

x_list=[]

def function(r):
	x0=0.001      ##initial x value to seed
	for i in range(0,500):
		xn=r*x0*(1-x0)     #f(x)
		x_list.append(xn)    #adds value to list
		x0 = xn            ##restarts loop using the value of xn
	plt.plot(r,x_list[-1],'--bo')     ##plots last value of xn vs r
while r<3.859:             ##adjusted this value to "zoom in" without losing point resolution
	r+= .000007       
	function(r)     #call the function for iterating values of r


plt.xlabel("r")
plt.ylabel("Xn")
plt.title("Crisis Region")
plt.show()
