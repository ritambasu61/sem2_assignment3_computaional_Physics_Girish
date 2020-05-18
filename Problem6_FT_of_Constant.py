#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:56:00 2020

@author: ritambasu
"""
import numpy as np
from matplotlib import pyplot as plt
#Problem1

def f(x):
    c=50
    return c

 
#fourier transform through dft by using numpy.fft by using the progamming meterial taught in the class 
xmin=-5
xmax=5
numpoints=1024
dx=(xmax-xmin)/(numpoints-1)
sampled_data=np.zeros(numpoints)
xarr=np.zeros(numpoints)
for i in range (numpoints):
    sampled_data[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx
dft=np.fft.fft(sampled_data,norm='ortho')
k=2*np.pi*np.fft.fftfreq(numpoints,d=dx)
factor=np.exp(-1j*k*xmin)
ft=dx*np.sqrt(numpoints/(2.0*np.pi))*factor*dft


#plottings
plt.plot(k,ft,label="numerical solution",ls='--')
plt.xlabel('k',fontsize=15)
plt.ylabel('ƒ˜(k)',fontsize=15)
plt.title('Fourier transform of f(x)(=costant=50) graph ',fontsize=15)
plt.legend()
plt.show()

t=np.arange(-50,50,0.01)
g=[]
for i in range(len(t)):
    g.append(f(t[i]))
plt.plot(t,g,label="actual fn in real space")
plt.legend()
plt.xlabel('x',fontsize=15)
plt.ylabel('f(x)',fontsize=15)
plt.title('x vs f(x) graph',fontsize=15)
plt.show()