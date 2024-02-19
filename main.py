#This script is written to create a Picket Chart used for lithology discrmination. 
import numpy as np
import matplotlib.pyplot as plt

#import csv file that has Well A velocity data
velocities_reciprocal = np.genfromtxt('Well_A_Velocities.csv', delimiter=',', skip_header=1)

svelocity_reciprocal = velocities_reciprocal[:, 0]  #P-wave Velocity in Km/sec
pvelocity_reciprocal  = velocities_reciprocal[:, 1]  #S-wave Velocity in Km/sec



#create data for ploting chart lines
sonic= np.arange(40, 120, 10)
shear_sonic= np.arange(90, 180, 10)

#create each line that has a specific value for Vp/Vs
line1=np.empty(8)
line2=np.empty(8)
line3=np.empty(8)
line4=np.empty(8)
for i in range (0, len(sonic)):
    line1[i]=1.6*sonic[i]
    line2[i]=1.7*sonic[i]
    line3[i]=1.8*sonic[i]
    line4[i]=1.9*sonic[i]

#create a label for each line. 
labels=['Vp/Vs = 1.6', 'Vp/Vs = 1.6','Vp/Vs = 1.8', 'Vp/Vs = 1.9' ]

#ploting lines and Well A data
fig, ax = plt.subplots(1, 1, figsize=(10, 7))
fig.set_facecolor('violet')
for i in range (0, len(sonic)):
    plt.plot(line1 , sonic,  linewidth=1.5, color='blue')
    plt.plot(line2 , sonic,  linewidth=1.5, color='orange')
    plt.plot(line3 , sonic,  linewidth=1.5, color='green')
    plt.plot(line4 , sonic,  linewidth=1.5, color='red')

ax.set_xlim(90,180)
ax.set_ylim(50,90)
ax.invert_yaxis()
ax.scatter(svelocity_reciprocal, pvelocity_reciprocal, marker='o', c='r')
ax.grid()
plt.legend(labels, prop={'size': 16})
plt.title('Picket Chart', fontsize = 18 )
ax.set_xlabel( '1/Vs (usec/ft)', fontsize = 16)
ax.set_ylabel( '1/Vp (usec/ft)', fontsize = 16)

plt.savefig('image.png')