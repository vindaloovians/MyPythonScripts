# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:35:59 2020

@author: Louis
"""

BendingLimit = 75 #3x EI
TorsionalLimit = 80 #4x TL/theta
#Invariant constants
l = 0.32 # Length
w = 0.05 # Width
#Thickness/Depth
bt = float(input("What thickness do you want your balsa wood to be in mm? "))/1000 #Balsa wood Thickness

btmm = bt*1000

#Now starting with the bending calculation

E = 2*10**9 #This can be anywhere between 2e9-5e9

twobt = 2*bt

t = 0.02 #Starting thickness/Depth of beam structure

BendingValue = (E*(((w)*(t)**3)-((w-twobt)*(t-twobt)**3))/12)

while BendingValue < 75:
    t = t + 0.001
    BendingValue = (E*(((w)*(t)**3)-((w-twobt)*(t-twobt)**3))/12)
    
tmm = t*1000 #Converting from m to mm

#Now continuing with the torsion calculations

G = 0.2*10**9 #This can be anywhere between 0.2e9 and 0.5e9

A = w*t
Asq = A**2
P = 2*(w+t)

TorsionValue = (4*Asq*G*bt)/P

while TorsionValue < 84:
    t = t + 0.001
    A = w*t
    Asq = A**2
    P = 2*(w+t)
    TorsionValue = (4*Asq*G*bt)/P

tmm = t*1000

print()
print('Assuming that the beam is purely balsa wood of a thickness',btmm,'mm')
print()
print('EI = ',BendingValue)
print('L/theta =',TorsionValue)
print('The optimum thickness is', round(tmm, 2), 'mm')

#Now to calculate the mass

P = 150 #Density of balsa wood is anywhere between 100-200
Vo = l*w*t
Vi = (l-twobt)*(w-twobt)*(t-twobt)
V = Vo - Vi
M = P*V

Mg = M*1000

print('Mass of beam is',Mg,'g')