import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
import time

# random number using np.random.rand
t0=time.time()
num=10000
randnum=np.random.rand(num)**1
t1=time.time()

print(t1-t0)

plt.hist(randnum,density=True,label='python generator')

# uniform pdf
x=np.linspace(0,1,10000,endpoint=True)
plt.plot(x,uniform.pdf(x),'r',label='uniform pdf')
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.legend(fontsize=4,loc='upper right')
plt.savefig('q#2.png',dpi=500)
plt.show()
