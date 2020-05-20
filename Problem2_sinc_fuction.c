#include <stdio.h>    
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>

//The given sinc function
float f(float x)
{
	if(x==0)
		return(1.0);
	else
	{
		float sinc;
		sinc=sin(x)/x;
		return(sinc);
	}
}

int  main()
{       //coded from C code note tought in lecture 15
  int numpoints=1024;float xmin=-500, xmax=500, dx=(xmax-xmin)/(numpoints-1), xarr[numpoints], k, aft_real, aft_imaginary, aft_absolute;
	fftw_complex w_p[numpoints], tw_q[numpoints];fftw_plan p;int i;

	for(i=0; i<numpoints; i++)
	{
		xarr[i]=xmin+i*dx;
		w_p[i][0]=f(xarr[i]); w_p[i][1]=0.0; 
	}	

	p=fftw_plan_dft_1d(numpoints, w_p, tw_q, FFTW_FORWARD, FFTW_ESTIMATE); //computing dft using fftw 	
	fftw_execute(p);
	
	FILE *data;
	data=fopen("Q2.txt","w");  //storing the numerical result for python plot
	
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
		//multiplying factors to covert dft to fourier transform
		aft_real=dx*sqrt(1/(2*M_PI))*(cos(k*xmin)*tw_q[i][0]+sin(k*xmin)*tw_q[i][1]);
	   	aft_imaginary= dx*sqrt(1/(2*M_PI))*(cos(k*xmin)*tw_q[i][1]-sin(k*xmin)*tw_q[i][0]);
		aft_absolute=sqrt(pow(aft_real,2)+pow(aft_imaginary,2));	
		fprintf(data,"%f    %f\n",k,aft_absolute);
	}
	
	fclose(data);	

	fftw_destroy_plan(p);
	return (0);
}

// gcc -o exec Q2.c -lfftw3 -lm
// ./exec
