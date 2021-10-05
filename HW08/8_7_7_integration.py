#written using python2.7 (filename changed .py-->.txt)


import numpy as np
import matplotlib.pyplot as plt

def integrate(x):    #integrate as a function of theta (theta=x)
	dx=.01  
	time=0   #initial time
	t_list=[]  
	theta_list=[]
	dt=.01
	x0=x  #variable to store labels
	i=0
	while i<4000*np.pi:    
		i+=1
		dxdt=np.sin(time)-np.sin(x)   #function to integrate
		x+= dxdt*dt     #euler stepping
		time+=dt          
		t_list.append(time)      
		theta_list.append(x)
		#plt.plot(time,x,'--bo') 
		if time>2*np.pi:        ##if statement that repeats the loop continuing to 					##iterate over theta but resetting time, 						##effectively creating the return map for 						##different cycles
			time=0
	plt.plot(t_list,theta_list, label=x0)
	plt.xlabel("Time")
	plt.ylabel("Theta")
	plt.title("Return map 8.7.7")
			
q=np.linspace(0,2*np.pi)    #generate t=theta line
plt.plot(q,q)		

n=1
for n in range(0,6):    #plots the function for several starting values of theta
	integrate(n)
plt.legend()
plt.show()


