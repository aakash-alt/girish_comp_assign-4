import numpy as np
import matplotlib.pyplot as plt
import scipy.stats 

ps=np.array([1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36])
count1=np.array([4,10,10,13,20,18,18,11,13,14,13])
count2=np.array([3,7,11,15,19,24,21,17,13,9,5])
n=sum(count1)
nps=n*ps # expected number of count
k=len(count1)-1 # degree of freedom

# calculating X^2-statistics

# for count1
chisq=sum((count1-nps)**2/nps)
test=1-scipy.stats.chi2.cdf(chisq,k)
test*=100
print('chi2 test for count1:\t',test,'%')
print('not sufficiently random') # this i got after looking value of 'test'

# for count2	
chisq=sum((count2-nps)**2/nps)
test=1-scipy.stats.chi2.cdf(chisq,k)
test*=100
print('chi2 test for count2:\t',test,'%')
print('not sufficiently random') # this i got after looking value of 'test'
	
