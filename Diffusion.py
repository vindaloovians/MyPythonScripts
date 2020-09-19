import math
import numpy as np
import matplotlib.pyplot as plt

T = 900+273
sigma = 0.02
M1 = 0.2
M2 = 0.7
D0 = 10**8
Q = 284000
R = 8.314

D = D0*np.exp(-Q/(R*T)) #Diffusion equation

def main():
    
    Xmin = 0
    Xmax = 1
    NX = 100
    dX = (Xmax-Xmin)/NX
    
    X = np.zeros([NX]) #creating an empty array
    
    for i in range(0, NX-1,1): #going from 0 to NX in steps of 1
        X[i] =  i*dX #as i increases, it is assigned a value
    
    tmin = 0
    Nt = 1000
    dt = 1
    
    t = np.zeros([Nt]) #creates an array going from 0 to 700 s with 0.1s incriments
    
    for j in range(0, Nt-1,1):
        t[j] = tmin + j*dt
    
    C = np.zeros([NX,Nt])
    
    for i in range(0, NX-1,1):
        C[i,0] = 1/np.sqrt(2*np.pi*sigma)*((math.exp(-((X[i]-M1)**2)/(2*sigma**2)))+math.exp(-((X[i]-M2)**2)/(2*sigma**2)))

        
    for j in range(0,Nt-1,1):
        t[j+1] = t[j] + dt
        
        for i in range(0,NX-1,1):
            C[i,j+1] = C[i,j]+((dt*D)/(dX)**2)*(C[i+1,j]-2*C[i,j]+C[i-1,j])
            
    plt.plot(X, C[:,0], label='Time = 0s')
    plt.plot(X, C[:,50], label='Time = 50s')
    plt.plot(X, C[:,300], label='Time = 300s')
    plt.plot(X, C[:,700], label='Time = 700s')
    plt.legend()
    plt.title('The Extent of Diffusion for Different Times at 900 deg C')
    plt.xlabel('position X/um')
    plt.ylabel('concentration c(X,t)')

main()
