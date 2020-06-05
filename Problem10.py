#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:07:27 2020

@author: ritambasu
"""


import numpy as np
#import pandas as pd # Import pandas
from matplotlib import pyplot as plt
from urllib.request import urlretrieve # Import package

# Assign url of file: url
url = 'http://theory.tifr.res.in/~kulkarni/noise.txt'
#coverting data to array
sampled_data=np.loadtxt(url)
 
#fourier transform through dft by using numpy.fft.fft 
xmin=0
dx=1
numpoints=len(sampled_data)
dft=np.fft.fft(sampled_data,n=numpoints,norm='ortho')
k=2*np.pi*np.fft.fftfreq(numpoints,d=dx)


"""Now the following process for convoluting R i.e
correlation fuction by convolution sampled data function with itself using
numpy.Though the same code can be use for conlvolution as spcified in problem 9"""


#power spectrum through convolution of R = colrelation function
#defining frequency array kq to plot dft w.r.t it
kq=np.fft.fftfreq(numpoints,d=dx)

#defining fourier transformed variable say(k) corresponding to data points say(x)
k=2*np.pi*kq
factor1=np.exp(-1j*k*xmin)

#Defining corelation function using Periodogram estimator
R=np.convolve(sampled_data,sampled_data,'same')/(2*numpoints) 

#Defining power spectrum to be forier transform of the correlation function
Power=np.abs(dx*np.sqrt(numpoints/(2.0*np.pi))*factor1*np.fft.fft(R,norm='ortho'))




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

#plotting the power spectrum bins
bins=10
plt.hist(Power,bins) 
plt.title('Actual Binned power spectrum ',fontsize=15)
plt.xlabel(r'Power spectrum',fontsize=16)
plt.ylabel(r'Occurance',fontsize=16)
plt.show()


#plotting of power spectrum through ft
f_k=dx*np.sqrt(numpoints/(2.0*np.pi))*factor1*dft
p=np.abs(f_k)**2/numpoints #power spectrum using Periodogram estimator
plt.plot(k,p)
plt.title('Power Spectrum through FT ',fontsize=15)
plt.ylabel('non_stocastic power spectrum',fontsize=16)
plt.xlabel('n',fontsize=16)
plt.show()

#plotting the power spectrum bins if the process were non stocastic
bins=10
plt.hist(p,bins) 
plt.title('Binned power spectrum Power Spectrum through FT',fontsize=15)
plt.xlabel(r'Power spectrum',fontsize=16)
plt.ylabel(r'Occurance',fontsize=16)
plt.show()
