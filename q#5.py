import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

num=10000
x1=np.random.rand(num)
x2=np.random.rand(num)
y1=np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2=np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

plt.hist(y1,density='True',color='c',label='Box-Muller distribution')

x=np.linspace(-4,4,10000,endpoint=True)
y=norm.pdf(x,loc=0,scale=1)
plt.plot(x,y,'k',label='norm-pdf')
plt.legend(fontsize=5)
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.savefig('q#5.png',dpi=500)
plt.show()
