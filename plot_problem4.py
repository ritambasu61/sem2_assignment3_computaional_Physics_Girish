#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:10:50 2020

@author: ritambasu
"""

import numpy as np
import matplotlib.pyplot as plt

#Exact result calculated analytically
def exact_ft(k):
    return(np.exp(-k*k/4.0)/np.sqrt(2.0))

#coverting txt file to array
data=open('Q4.txt','r')
karr=[]
aft=[]
aft_exact=[]

for line in data:
    k,aft_data=line.split()
    karr.append(float(k))
    aft.append(float(aft_data))
    aft_exact.append(exact_ft(float(k)))

plt.plot(karr,aft,'r',label='numerical result')    
plt.plot(karr,aft_exact,'black',label='analytical result')
plt.xlabel('k',fontsize=16)
plt.ylabel(r'$\tilde{f}$',fontsize=16)
plt.title('Comparison of results ',fontsize=15)
plt.legend()
plt.show()
