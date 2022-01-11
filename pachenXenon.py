import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
from scipy.interpolate import interp1d
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline
import numpy as np

x=[0.5,0.6,0.7,0.8,0.9,1,2,3,5,7,10,20,30,50,70,100,200,300,500,700,1000]
Air=[360,350,360,370,380,400,500,630,750,1000,1400,1900,2600,3100,4000,6000,10000,17000,24000,30000,40000]
Xenon=[1000,800,700,650,610,600,490,500,510,520,600,690,850,1200,1600,1900,2800,4000,7500,10000,14000]

f2=InterpolatedUnivariateSpline(x,Air)
f3=InterpolatedUnivariateSpline(x,Xenon)
xnew=np.linspace(0.5,1000,num=1000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.yscale('log')
#plt.xscale('log')
ax.plot(x, Air, color='tab:blue')
ax.plot(xnew, f2(xnew), color='tab:green',label='Air')
ax.plot(x, Xenon, color='tab:pink')
ax.plot(xnew, f3(xnew), color='tab:orange',label='Xenon')
ax.set_xlabel('Pressure x electrode spacing (Torr X cm)')
ax.set_ylabel('Discharge Voltage (V)')
ax.legend()
plt.show()
