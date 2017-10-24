import matplotlib.pyplot as plt
import math
import numpy as np

vo=int(input("Enter the initial velocity for trajectory 1(m/s)  : "))
angle=int(input("Enter the angle of projection for trajectory 1 (degrees)  : "))
rad=(math.pi/180)*angle
tf=2*vo*(math.sin(rad))/9.81
h=(vo**2)*((math.sin(rad))**2)/(2*9.81)
r=(vo**2)*(math.sin(2*rad))/9.81
vxo=vo*(math.cos(rad))
vyo=vo*(math.sin(rad))
numx=[]
numy=[]
for t in (np.arange(0, int(tf), 0.1)):
    xdist = vo * t
    xvelo = vxo
    ydist = (vyo * t) - (9.81 * t ** 2) / 2
    yvelo = vyo - (9.81 * t)
    numx.append(xdist)
    numy.append(ydist)

plt.plot(numx,numy,color='blue')

vo1=int(input("Enter the initial velocity for trajectory 2(m/s)  : "))
angle1=int(input("Enter the angle of projection for trajectory 2 (degrees)  : "))
rad1=(math.pi/180)*angle1
tf1=2*vo1*(math.sin(rad1))/9.81
h1=(vo1**2)*((math.sin(rad1))**2)/(2*9.81)
r1=(vo1**2)*(math.sin(2*rad1))/9.81
vxo1=vo1*(math.cos(rad1))
vyo1=vo1*(math.sin(rad1))
numx1=[]
numy1=[]
for t1 in (np.arange(0, int(tf1), 0.1)):
    xdist1 = vo1 * t1
    xvelo1 = vxo1
    ydist1 = (vyo1 * t1) - (9.81 * t1 ** 2) / 2
    yvelo1 = vyo1 - (9.81 * t1)
    numx1.append(xdist1)
    numy1.append(ydist1)

plt.plot(numx1,numy1,color='green')

vo2=int(input("Enter the initial velocity for trajectory 3 (m/s)  : "))
angle2=int(input("Enter the angle of projection for trajectory 3 (degrees)  : "))
rad2=(math.pi/180)*angle2
tf2=2*vo2*(math.sin(rad2))/9.81
h2=(vo2**2)*((math.sin(rad2))**2)/(2*9.81)
r2=(vo2**2)*(math.sin(2*rad2))/9.81
vxo2=vo2*(math.cos(rad2))
vyo2=vo2*(math.sin(rad2))
numx2=[]
numy2=[]
for t2 in (np.arange(0, int(tf2), 0.1)):
    xdist2 = vo2 * t2
    xvelo2 = vxo2
    ydist2 = (vyo2 * t2) - (9.81 * t2 ** 2) / 2
    yvelo2 = vyo2 - (9.81 * t2)
    numx2.append(xdist2)
    numy2.append(ydist2)

plt.plot(numx2,numy2,color='red')




plt.show()

