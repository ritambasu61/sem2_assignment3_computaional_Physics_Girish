#include <stdio.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>
#define real(z,i) ((z)[2*(i)])
#define imaginary(z,i) ((z)[2*(i)+1])

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
		real(data,i)=f(xmin+i*dx); imaginary(data,i)= 0.0;
	}

	gsl_fft_complex_radix2_forward (data, 1, n); 

        //command for save the data in a txt file
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

		real(data,i)=dx*(1/sqrt(2.0*M_PI))*(cos(k[i]*xmin)*real(data,i)+sin(k[i]*xmin)*imaginary(data,i));
		
		fprintf(fptr,"%f    %f\n",k[i],real(data,i));		
	}
	
	fclose(fptr);	

	return 0;
}

// gcc -Wall Q3.c -lm -lgsl -lgslcblas -o Q3
// ./Q3
