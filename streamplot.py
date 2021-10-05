##written in python 2.7


import matplotlib.pyplot as plt 
import numpy as np

x=y=np.linspace(-10,10)

X,Y=np.meshgrid(x,y)

mew=-10
xdot=-Y+mew*X+X*Y**2
ydot=X+mew*Y-X**2

plt.streamplot(X,Y,xdot,ydot)
plt.title("Mu=1")
plt.show()
