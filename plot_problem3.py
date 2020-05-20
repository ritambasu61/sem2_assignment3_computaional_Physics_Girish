#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:14:43 2020

@author: ritambasu
"""
import numpy as np
import matplotlib.pyplot as plt

#the analytical result
def exact_ft(k):
    if(abs(k)<1.0 and k>-1.0):
        return(np.sqrt(np.pi/2.0))
    else:
        return(0.0)

file=open('Q3.txt','r')
karr=[]
aft=[]
aft_exact=[]

for line in file:
    k,aft_data=line.split()
    karr.append(float(k))
    aft.append(float(aft_data))
    aft_exact.append(exact_ft(float(k)))

plt.plot(karr,aft,'.r',label=r'numerical result')    
plt.plot(karr,aft_exact,'black',label='analytical result')
plt.xlabel('k',fontsize=16)
plt.ylabel(r'$\tilde{f}$',fontsize=16)
plt.title('Comparison of results ',fontsize=15)
plt.legend()
plt.show()
