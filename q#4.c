#include<stdio.h>
#include<math.h>

// defining function for generating random number from 0 to 1
double randgen(void)
{
	return (rand()%RAND_MAX)/(double)RAND_MAX;
}
// defining function for exponential pdf
double transform(double x)
{
	double lambda=2.; // decay rate of exponential-decay (=1/mean)
	return -lambda*log(1-x);
}
int main()
{
	int num=10000;
	double randnum[num];
	for(int i=0;i<num;++i)
	{
		randnum[i]=randgen();
		randnum[i]=transform(randnum[i]);
		printf("%lf\n",randnum[i]);
	}
}
