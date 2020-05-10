#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:26:05 2020

@author: ritambasu
"""
import timeit
from matplotlib import pyplot as plt
import numpy as np
#defining n
def g(n):
    starttime2=timeit.default_timer()
    wp=np.arange(0,n,1)
    dft_arr_num = np.fft.fft(wp,norm='ortho')
    t_numpy_code=timeit.default_timer()-starttime2
    return(t_numpy_code)
def f(n):
    starttime=timeit.default_timer()
    wp=np.arange(0,n,1)
    numpoints=len(wp)
    dft_list=[]
    for q in range (numpoints):
        dft=0
        for p in range (numpoints):
            dft=dft+wp[p]*np.exp(-1j*2*np.pi*p*q/n)
        dft=(1/np.sqrt(n))*dft
        dft_list.append(dft)
    t_my_code=timeit.default_timer()-starttime
    #print("Time taken by my code is:", t_my_code,"start time:",starttime)
    return(t_my_code)
           
        
k=np.arange(4,101,1)
my_time_arr=np.zeros(len(k))
numpy_time_arr=np.zeros(len(k))
for i in range(len(k)):
    my_time_arr[i]=f(k[i])
    numpy_time_arr[i]=g(k[i])
plt.plot(k,my_time_arr,label="Tme taken by my code")
plt.plot(k,numpy_time_arr,label="Tme taken by numpy.fft.fft")
plt.xlabel('n',fontsize=15)
plt.ylabel('time',fontsize=15)
plt.title('Time comparison between ',fontsize=20)
plt.legend()
plt.show()

       
    
    
    
        
      
      
    
