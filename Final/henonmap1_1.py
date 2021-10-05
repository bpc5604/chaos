import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
yi=0
xi=0
a=1.4
b=.3
for i in range (1,10000):
    x1=yi+1-a*xi**2  #x_n +1
    y1=b*xi          #y_n +1
    x.append(x1)
    y.append(y1)
    xi=x1
    yi=y1
    i +=1
    plt.plot(xi,yi,'b.-')
plt.title('Henon Map')
plt.show()
