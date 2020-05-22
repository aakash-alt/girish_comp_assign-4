import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import emcee
import corner

data=np.loadtxt('q#10data.txt',delimiter='&')
x=data[:,1]
y=data[:,2]
sigmay=data[:,3] # sometime it'll be called as yerr 

# defining log of likelihood (Gaussian) function
def log_likelihood(theta,x,y,yerr):
	a,b,c=theta
	model=a*x**2+b*x+c
	sigma2=yerr**2
	return 0.5*np.sum((y-model)**2/sigma2+np.log(2*np.pi*sigma2))
# defining log of prior (uniform) probability distribution
def log_prior(theta):
	a,b,c=theta
	if (-500<a<500 and -500<b<500 and -500<c<500):
		return 0
	return -np.inf
# defining log of posterior probability distribution
# although actual formula consist of a term ( p(data|thoery) ) in its denominator which is a constant, but while MCMC sampling we don't care about such normalising constants😎️😎️.
def log_probability(theta,x,y,yerr):
	lp=log_prior(theta)
	if not np.isfinite(lp):
		return -np.inf
	return lp-log_likelihood(theta,x,y,yerr)
guess=(1,1,1)
soln=minimize(log_likelihood,guess,args=(x,y,sigmay))
# 50 Markov chain
nwalkers,ndim=50,3
pos=soln.x+1e-4*np.random.randn(nwalkers,ndim)
sampler=emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x,y,sigmay))
sampler.run_mcmc(pos,4000)
samples=sampler.get_chain()
tau=sampler.get_autocorr_time() # this gives the 'burn in' time (no. of steps)
plt.plot(samples[:,:,0])
plt.ylabel('$a$')
plt.xlabel('nsteps')
plt.savefig('params_a.png',dpi=500)
plt.show()
plt.plot(samples[:,:,1])
plt.ylabel('$b$')
plt.xlabel('nsteps')
plt.savefig('params_b.png',dpi=500)
plt.show()
plt.plot(samples[:,:,2])
plt.ylabel('$c$')
plt.xlabel('nsteps')
plt.savefig('params_c.png',dpi=500)
plt.show()
# let's get the flat list of samples
# tau suggests number of steps required for burn-in, so we can safely ignore few times of burn-in steps, and thin it by half (appox.) of the burn-in steps.
flat_samples=sampler.get_chain(discard=100,thin=15,flat=True)
medians=np.median(flat_samples,axis=0)
a_true,b_true,c_true=medians
labels=['a','b','c']
infile=open('params.txt','w')
print('params\ttrue value\t1sigma-up\t1sigma-down',file=infile)
for i in range(ndim):
	mcmc = np.percentile(flat_samples[:, i], [16, 50, 84])
	q = np.diff(mcmc)
	print(labels[i],'\t',round(mcmc[1],5),'\t',round(q[1],5),'\t',round(-q[0],5),file=infile)
infile.close()
fig=corner.corner(flat_samples,labels=labels)
plt.savefig('joint-marginalised-pdf.png',dpi=500)
plt.show()
indx=np.random.randint(len(flat_samples),size=200)
for i in indx:
	params=flat_samples[i]
	ind=np.argsort(x)
	plt.plot(x[ind],params[:3][0]*x[ind]**2+params[:3][1]*x[ind]+params[:3][2],'C1',alpha=.1)
ind=np.argsort(x)
plt.plot(x[ind],a_true*x[ind]**2+b_true*x[ind]+c_true,'k',label='true')
plt.errorbar(x,y,yerr=sigmay,fmt='.k')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(fontsize=8)
plt.title('best quadratic fit to data', fontsize=8)
plt.savefig('datafit.png',dpi=500)
plt.show()	
