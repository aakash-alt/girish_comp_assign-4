import numpy as np
import matplotlib.pyplot as plt

num=10000000

# area of the circle
A=1 # area of square in the first quadrant with a=1
x=np.linspace(0,1,num,endpoint=True)
y=np.zeros(num)
y[1:num-1]=1
xrand=np.random.rand(num)
yrand=np.random.rand(num)
r=np.sqrt(xrand**2+yrand**2) # radius of circle
# selecting desirable points
xgood=xrand[r<=1]
ygood=yrand[r<=1]
goodnum=len(xgood) # number of desirable points
frac=goodnum/num 
area=frac*A
area*=4 # area of the total circle is 4*area in one quadrant
print('area of the unit circle:',area,'square units')


# volume of tenD sphere
V=1 # volume of the unit cube in the first dodecant 
xrand1=np.random.rand(num)
xrand2=np.random.rand(num)
xrand3=np.random.rand(num)
xrand4=np.random.rand(num)
xrand5=np.random.rand(num)
xrand6=np.random.rand(num)
xrand7=np.random.rand(num)
xrand8=np.random.rand(num)
xrand9=np.random.rand(num)
xrand10=np.random.rand(num)
R=np.sqrt(xrand1**2+xrand1**2+xrand1**2+xrand1**2+xrand1**2
+xrand1**2+xrand1**2+xrand1**2+xrand1**2+xrand1**2) # radius of 10-dim sphere
xgood1=xrand1[R<=1]
goodnum=len(xgood1)
frac=goodnum/num
volume=frac*V
volume*=2**10 # total volume is 2^10* volume in one dodecant
print('volume of tenD sphere is:',volume,'unit^10')
