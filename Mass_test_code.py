# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import iv

def sigma(x,tau):
    return (((1/tau)*x**(1/4)*(np.exp(-(1+x**2)/tau))*iv(1/4,x))

g=np.linspace(0,1,10)
print(g)

u=np.linspace(0,3,100)
for i in range g:
    plt.plot(u,sigma(u,tau),label=ig)
            
plt.legend(fontsize=12,loc='best')
plt.xlabel('x',fontsize=15)
plt.ylabel('J_0(x)',fontsize=15)
plt.show()