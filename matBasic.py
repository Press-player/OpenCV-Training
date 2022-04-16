import matplotlib.pyplot as plt
import numpy as np
x =np.linspace(0,2*np.pi,40)
y =np.sin(x)
y2 =np.cos(x)
plt.grid(True)
plt.xlabel('My X values')
plt.ylabel("My Y values")
plt.title("My first graph")
#plt.axis([0,9,0,9])
plt.plot(x,y,'g-o',label="Sin(x)")
plt.plot(x,y2,'b-*',linewidth=2,markersize=6,label='Cos(x)')
plt.legend(loc="upper center")
plt.show()
