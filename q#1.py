import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import time


# random number using Congruential Linear generator
t0=time.time()
seed=1
increment=1013904223
multiplier=1664525
modulus=4294967296

n=10000
results=[]
for i in range(n):
	seed=(multiplier*seed+increment)%modulus
	x0=seed
	seed=(multiplier*seed+increment)%modulus
	x1=seed
	randnum=min(x0,x1)/max(x0,x1)
	results.append(randnum)
t1=time.time()
print(t1-t0)
x=np.linspace(0,1,10000,endpoint=True)
plt.hist(results,color='c',density=True,label='CLG-numbers') # uniform pdf
plt.plot(x,uniform.pdf(x),'r',label='uniform pdf')
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.legend(fontsize=4,loc='upper right')
plt.savefig('q#1.png',dpi=500)
plt.show()

