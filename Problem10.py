#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:07:27 2020

@author: ritambasu
"""


import numpy as np
import pandas as pd # Import pandas
from matplotlib import pyplot as plt
from urllib.request import urlretrieve # Import package

# Assign url of file: url
url = 'http://theory.tifr.res.in/~kulkarni/noise.txt'
#coverting data to array
sampled_data=np.loadtxt(url)
 
#fourier transform through dft by using numpy.fft.fft 
dx=1
numpoints=len(sampled_data)
dft=np.fft.fft(sampled_data,n=2*numpoints,norm='ortho')
k=2*np.pi*np.fft.fftfreq(2*numpoints,d=dx)


"""Now the following process for convoluting R i.e
corelation fuction by convolution sampled data function with itself"""



#defining frequency array kq
kq=np.fft.fftfreq(2*numpoints,d=dx)

#defining fourier transformed variable say(k) corresponding to data points say(x)
k=2*np.pi*kq

#defining x array which is in the inverse fourier space of k array
dk=k[3]-k[2]
x=2*np.pi*np.fft.fftfreq(2*numpoints,d=dk)

#multiplying two dft's with approaite factors
xmin=0
factor1=np.exp(-1j*k*xmin)
g_ddft=(factor1*dft)
h_ddft=(factor1*dft)

"""multiplying two dft's and taking the inverse fourier transform using numpy.fft.ifft
 to compute the convolution """
mult_dft=(g_ddft*h_ddft)
#Defining corelation function using Periodogram estimator
R=(dx*np.sqrt(2*numpoints)*np.fft.ifft(mult_dft,norm='ortho')/numpoints) 
#defining power spectrum to be forier transform of the correlation function
Power=np.abs(dx*np.sqrt(numpoints/(2.0*np.pi))*factor1*np.fft.fft(R,norm='ortho'))/numpoints



#plotting of sampled data
plt.plot(sampled_data)
plt.xlabel('n',fontsize=16)
plt.ylabel('sampled function value',fontsize=16)
plt.show()



#plotting of dft of sampled data
plt.plot(kq,dft)
plt.title('DFT ',fontsize=15)
plt.xlabel('kq',fontsize=16)
plt.ylabel('DFT of  function value',fontsize=16)
plt.show()

#plotting of power spectrum
plt.plot(k,Power)
plt.title('Power Spectrum ',fontsize=15)
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'Power spectrum',fontsize=16)
plt.show()


#plotting of power spectrum if the process is non-stocastic
f_k=dx*np.sqrt(numpoints/(2.0*np.pi))*factor1*dft
p=(np.conj(f_k)*f_k)/numpoints #power spectrum using Periodogram estimator
plt.plot(k,p)
plt.title('for Non Stocastic process Power Spectrum ',fontsize=15)
plt.ylabel('non_stocastic power spectrum',fontsize=16)
plt.xlabel('n',fontsize=16)
plt.show()

#plotting the power spectrum bins
bins=10
plt.hist(Power,bins) 
plt.xlabel(r'Power spectrum',fontsize=16)
plt.ylabel(r'Occurance',fontsize=16)
plt.show()
