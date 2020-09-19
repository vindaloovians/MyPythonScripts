import random
import numpy
nmoves = input('Please state how many times you want the particle to move: ')
temperature = int(input('What temperature will the experiment be run at: ')) #in this experiment it is 1273K but you might want to change this
print() #to separate the output and make it look nice on the console
N = int(nmoves) #I will now create a 2d array of all possible moves
delta = [[0.18, 0.18, 0],[0.18, 0, 0.18],[0, 0.18, 0.18],[-0.18, 0.18, 0],[0.18, -0.18, 0],[-0.18, 0, 0.18],[0.18, 0, -0.18],[0, -0.18, 0.18],[0, 0.18, -0.18],[-0.18, -0.18, 0],[-0.18, 0.00, -0.18],[0.00, -0.18, -0.18]]
def path(N):
    xval,yval,zval = 0,0,0
    for i in range(N): 
        number = random.randint(0,11) #a random number is generated and this decides which move will be taken
        xval += delta[number][0] #I am now adding the chosen pathway to the x, y and z directions
        yval += delta[number][1]
        zval += delta[number][2]
    return [xval,yval,zval] #returning gives a list which can be used later
result = path(N)
R = (((result[0]**2)+(result[1]**2)+(result[2]**2))**0.5)*10**-9
t = 1/(12*10**13*numpy.exp(-0.99/(8.617*10**-5*temperature)))
D = (R**2)/(6*t)
print('Your particle has travelled',R,'metres in',t,'seconds')
print('The diffusivity is therefore',D,'m**2/s')