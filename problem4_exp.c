#include <stdio.h>    
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>

float f(float x)
{
	return(exp(-x*x));
}
//coded using class module
void main()
{
	int numpoints=512;
	float xmin=-100, xmax=100, dx=(xmax-xmin)/(numpoints-1), xarr[numpoints], k, aft_real, aft_img, aft_abs;fftw_complex w_p[numpoints], tw_q[numpoints];fftw_plan p;int i;

	for(i=0; i<numpoints; i++)
	{
		xarr[i]=xmin+i*dx;
		w_p[i][0]=f(xarr[i]); w_p[i][1]=0.0;
	}	

	p=fftw_plan_dft_1d(numpoints, w_p, tw_q, FFTW_FORWARD, FFTW_ESTIMATE);	
	fftw_execute(p);
	
	FILE *data;
	data=fopen("Q4.txt","w");
	

	for(i=0; i<numpoints; i++)
	{
		if(i<=(numpoints/2-1))
		{
			k=i/(numpoints*dx);
			k=2*M_PI*k;
		}
		else
		{
			k=(i-numpoints)/(numpoints*dx);
			k=2*M_PI*k;
		}
		aft_real=dx*sqrt(1/(2*M_PI))*(cos(k*xmin)*tw_q[i][0]+sin(k*xmin)*tw_q[i][1]);
	   	aft_img= dx*sqrt(1/(2*M_PI))*(cos(k*xmin)*tw_q[i][1]-sin(k*xmin)*tw_q[i][0]);
		aft_abs=sqrt(pow(aft_real,2)+pow(aft_img,2));	
		fprintf(data,"%f  %f\n",k,aft_abs);
	}
	
	fclose(data);	

	fftw_destroy_plan(p);
}

// gcc -o exec Q4.c -lfftw3 -lm
// ./exec
