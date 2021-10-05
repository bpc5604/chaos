import matplotlib.pyplot as plt
import numpy as np

x=y=np.linspace(-np.pi,2*np.pi,20)
#y=np.linspace(-10,10)

t=np.linspace(0,10,20)
W,T=np.meshgrid(x,y)


#X=np.meshgrid(-10:10)
#Y=np.meshgrid(-10:10)

a=0
xdot=np.sin(T)-np.sin(W)
ydot=1


#fig,ax=plt.subplots()
#q=ax.quiver(W,Z)
#ax.quiverkey(q,X=0.3,Y=1.1,U=10,label='key',labelpos='E')

plt.quiver(T,W,ydot,xdot,headlength=5)
plt.xlim(-np.pi,2*np.pi)
plt.ylim(-np.pi,2*np.pi)
plt.title("Mu=10")
plt.xlabel("Time")
plt.ylabel("Theta")
plt.show()
