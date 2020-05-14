#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 07:25:25 2020

@author: ritambasu
"""
import numpy as np
from matplotlib import pyplot as plt
#Problem1

def g(x):
    if abs(x)<1.0 and x>-1.0:
        return 1.0
    else :
        return 0.0
def h(x):
    if x<1.0 and x>-1.0:
        return 1.0
    else :
        return 0.0
#defining the exact convoluted f(x) calculated by using mathematica
def f(x):
    if x<0.0 and x>-2.0:
        return (x+2)
    if x>0.0 and x<2.0:
        return (-x+2)
    else:
        return 0.0
    
        

"""making array to compute dft by using numpy.fft by using the 
progamming meterial taught in the class """
xmin=-40
xmax=40
numpoints=1024
dx=(xmax-xmin)/(numpoints-1)
g_sampled_data=np.zeros(numpoints)
h_sampled_data=np.zeros(numpoints)
f_sampled_data=np.zeros(numpoints)#array to plot exact covoluted function
xarr=np.zeros(numpoints)
for i in range (numpoints):
    h_sampled_data[i]=h(xmin+i*dx)
    g_sampled_data[i]=g(xmin+i*dx)
    f_sampled_data[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx
#computing two dfts using numpy
g_dft=np.fft.fft(g_sampled_data,n=2*numpoints,norm='ortho')
h_dft=np.fft.fft(h_sampled_data,n=2*numpoints,norm='ortho')
k=2*np.pi*np.fft.fftfreq(2*numpoints,d=dx)

#defining x array which is in the inverse fourier space of k array
dk=k[3]-k[2]
x=2*np.pi*np.fft.fftfreq(2*numpoints,d=dk)

#multiplying two dft's with approaite factors
factor1=np.exp(-1j*k*xmin)
g_ddft=(factor1*g_dft)
h_ddft=(factor1*h_dft)

"""multiplying two dft's and taking the inverse fourier transform using numpy.fft.ifft
 to compute the convolution """
mult_dft=(g_ddft*h_ddft)
f_x=np.real(dx*np.sqrt(2*numpoints)*np.fft.ifft(mult_dft,norm='ortho'))

#plottings
plt.xlim(left=-5,right=5)
plt.ylim(bottom=0,top=3)
plt.scatter(x,f_x,label="numerical convolution",marker="o",s=15,color='Green')
plt.plot(xarr,f_sampled_data,label="analytical convolution",color='Black')
plt.plot(xarr,g_sampled_data,label="function before convolution",color='Red')
plt.title('Convolution',fontsize=20)
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)
plt.legend()
plt.show()