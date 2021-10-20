# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

Mf=1.4*1e23
tau=10*365*86400*1000
def Mass(Ms,t):
    
    dMsdt = 7.15*((Mf-Ms)/tau)*(Ms/Mf)**(2/3)
    return dMsdt
# initial condition
M0 = 1

# time points
t = np.linspace(0,365*84600,1000)

# solve ODE
Ms = odeint(Mass,M0,t)

# plot results
plt.plot(t,Ms)
plt.xlabel('time')
plt.ylabel('Ms(t)')
plt.show()