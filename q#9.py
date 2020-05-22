import numpy as np
import random
import matplotlib.pyplot as plt
from  scipy.stats import norm

# scaled pdf
def f(theta):
	if(theta>=3 and theta<=7):
		a=1 # scaled version of pdf which has been used for sampling
	else:
		a=0
	return a
# pdf
def p(theta):
	if(theta>=3 and theta<=7):
		a=0.25 # to make the distribution normalised
	else:
		a=0
	return a
nsteps=10000
theta=5
x=[]
theta1=[] # storing generated points @ each iteration
for i in range(nsteps):
	theta_prime=theta+np.random.standard_normal()
	theta1.append(theta_prime)
	r=np.random.rand()
	if (f(theta_prime)/f(theta)>r):
		theta=theta_prime
	x.append(theta)
# plotting MCMC-chain
plt.plot(theta1,'.r',label='generated point')
plt.plot(x,'.-k',label='sampled point')
plt.legend(loc='upper left',fontsize=4)
plt.title('MCMC-chain (sampled points are accepeted generated points @ each iteration )',fontsize=8)
plt.xlabel('nsteps')
plt.ylabel('sampled points')
plt.savefig('MCMCchain#10k.png',dpi=500) 
plt.show()
# plotting sampled distribution
xi=np.linspace(0,10,nsteps,endpoint=True)
fx=[]
px=[]
for i in range(nsteps):
	fx.append(f(xi[i]))
	px.append(p(xi[i]))
plt.hist(x,density=True,color='c',label='MCMC-sampling')
plt.plot(xi,fx,'k',label='scaled pdf')
plt.plot(xi,px,'r',label='pdf')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend(fontsize=8)
plt.savefig('q#9.png',dpi=500)
plt.show()

