# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:08:19 2020

@author: Louis
"""

import numpy as np
from random import randint
from random import uniform
from PIL import Image

Nx = 200 # Number of cells in 2D
Nt = 200 # Number of timesteps
Ng = 20 #Number of initial grains

s = np.zeros((Nx,Nx)) # Create array with Nx rows and Nx columns, all zeros
 
for g in range(1,Ng+1): # For the number of new grains...
    s[randint(0,Nx-1)][randint(0,Nx-1)] = g + 5# Assign new state to nuclei
 
frames = [] # Create empty list to store image frames

c = 0 #counter that will stop the simulation once all grains have crystallised

for t in range(1,Nt): # Loop through all timesteps 
    ps = np.copy(s)
    if c == Nx**2 - Ng:
        break #stops simulation
    for x in range(Nx): # Loop through all the cells in the system
        left = x-1 if x > 0 else Nx-1 # Find index of cell to the left
        right = x+1 if x < Nx-1 else 0 # Find index of cell to the right
        for y in range(Nx):
            down = y-1 if y > 0 else Nx-1
            up = y+1 if y < Nx-1 else 0
            neighbours = []
            adjneighbours = [ps[left][y], ps[right][y], ps[x][down], ps[x][up]]
            diagneighbours = [ps[left][down], ps[right][up], ps[right][down], ps[left][up]]
            if ps[x][y] == 0: #If cell hasn't recrystalised yet.
                for i in range(len(diagneighbours)):
                    if uniform(0,1) < 0.5: #essentially adjusts neighbourhood so grains don't preferentially grow diagonally - males them approximately circular
                        neighbours.append(diagneighbours[i])
                for j in range(len(adjneighbours)):
                    if uniform(0,1) < 0.9717:
                        neighbours.append(adjneighbours[j])
                if sum(neighbours) > 0:
                    z = [k for k, e in enumerate (neighbours) if e!=0] #searches for all non zero terms
                    s[x][y] = neighbours[z[randint(0,(len(z)-1))]]
                    c += 1
    rescaled = (255.0 / s.max() * s).astype(np.uint8) # Rescale to 0-255 and convert to uint8
    im = Image.fromarray(rescaled) # Create image from array
    frames.append(im) # Append image to frames

frames[0].save('output.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0) # Save frames to a gif file
