import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

rnum=np.loadtxt('q#4.dat')

plt.hist(rnum,color='c',density='True',label='exponential-distribution')

x=np.linspace(0,25,10000,endpoint=True)
y=expon.pdf(x,loc=0,scale=2)
plt.plot(x,y,'k',label='expon-pdf')
plt.legend(fontsize=8)
plt.savefig('q#4.png',dpi=500)
plt.show()
