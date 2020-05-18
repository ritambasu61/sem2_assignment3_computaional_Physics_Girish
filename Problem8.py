#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:34:00 2020

@author: ritambasu
"""
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
fig = plt.figure()
ax = plt.axes(projection="3d")
def f(x, y):
    return(np.exp(-(np.power(x,2)+np.power(y,2))))

#fourier transform using numpy.fft.fft2
def fk_exact(kx,ky):
    return(0.5*np.exp(-0.25*(np.power(kx,2)+np.power(ky,2))))
xmin=-5
xmax=5
ymin=-5
ymax=5
numpoints=1024
dx=(xmax-xmin)/(numpoints-1)
dy=(ymax-ymin)/(numpoints-1)
xarr=np.zeros(numpoints)
yarr=np.zeros(numpoints)
for i in range (numpoints):
        yarr[i]=ymin+i*dy
        xarr[i]=xmin+i*dx
Xarr, Yarr = np.meshgrid(xarr, yarr)
farr = f(Xarr,Yarr)
dft=np.fft.fft2(farr,norm="ortho")
kx=2*np.pi*np.fft.fftfreq(numpoints,d=dx)
ky=2*np.pi*np.fft.fftfreq(numpoints,d=dy)
KX,KY=np.meshgrid(kx,ky)
factor=np.exp(-1j*kx*xmin)*np.exp(-1j*ky*ymin)
FT=np.abs(dx*dy*(numpoints/(2.0*np.pi))*factor*dft)
Fk_Exact=fk_exact(KX,KY)

#plottings in 3d
ax.plot_wireframe(KX,KY ,FT, color='Red',label="Numerical solution")
ax.plot_wireframe(KX,KY,Fk_Exact, color='Green',label="Analytical solution")
ax.set_xlabel('kx',fontsize=15)
ax.set_ylabel('ky',fontsize=15)
ax.set_zlabel('ƒ',fontsize=15)
plt.title('kx,ky vs f`(kx,ky) graph',fontsize=15)
plt.legend()
plt.show()

