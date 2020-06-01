#include <stdio.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>
#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])

int n=1024;

double f(double x) 
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

int main (void)
{
	double xmin=-500.0, xmax=500.0, dx=(xmax-xmin)/(n-1), k[n], data[2*n];

	for (int i=0;i<n;i++)
	{
		REAL(data,i)=f(xmin+i*dx); IMAG(data,i)= 0.0;
	}

	gsl_fft_complex_radix2_forward (data, 1, n); 


	FILE *fptr;
	fptr=fopen("Q3.txt","w");
	
	int i;	
	for(i=0; i<n; i++)
	{
		if(i<=(n/2-1))
		{
			k[i]=2*M_PI*(i/(n*dx));
		}
		else
		{
			k[i]=2*M_PI*((i-n)/(n*dx));
		}

		REAL(data,i)=dx*(1/sqrt(2.0*M_PI))*(cos(k[i]*xmin)*REAL(data,i)+sin(k[i]*xmin)*IMAG(data,i));
		
		fprintf(fptr,"%f    %f\n",k[i],REAL(data,i));		
	}
	
	fclose(fptr);	

	return 0;
}

// gcc -Wall Q3.c -lm -lgsl -lgslcblas -o Q3
// ./Q3

