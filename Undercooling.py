import numpy as np
import pylab as pl

# Here is a prompt for the user to select which alloy they want. I just put this in for a bit of fun.

answer = input("Type in the first letter of the alloy that you wish to find the cricial radius of. Your options are 'IN718' and 'CM247LC'. ")
if answer == "I":
   print("You have chosen alloy IN718.")#
   name = "IN718"
   Tm = 1609
   L8 = 1.47e6
   Y = 1.88
   P = 7400
elif answer == "C":
   print("You have chosen alloy CM247LC.")
   name = "CM247LC"
   Tm = 1555
   L8 = 1.70e6
   Y = 1.82
   P = 8250
   
iterations = [] #creates a list for the iterations
errors = [] #creates a list for the errors
CR = [] #creates a list for the critical radii
temp = [] #creates a list for the dT values

X0 = 27e-9 #This is the intial best guess
tol = 1e-6
dT = 0 #dT is set to 0 as for each loop 20 will be added (including the first!).

def NR(dT):
    
    dT = dT + 20
    
    def f(X):
        value = ((-4*np.pi*(X)**2)*P*(L8*dT/Tm)) + ((8*np.pi*X*Y))
        return value

    def fi(X):
        value = ((-8*np.pi*(X)*P*(L8*dT/Tm)) + ((8*np.pi*Y)))
        return value

#X0 and tol are the variables we will need to consider

    def main(X0, tol):
        
        iter = 0
        iter_max = 100
        Xn1 = X0 - (f(X0)/fi(X0))
        print(Xn1)
        err = abs(Xn1 - X0)/Xn1

#Keep iterating until the error is lower than the tolerance

        while err > tol:
            
            if iter == 0:
                Xn2 = Xn1
        
            elif iter > 0:
                Xn1 = Xn2
                Xn2 = Xn1 - (f(Xn1)/fi(Xn1))
                err = abs(Xn2 - Xn1)/Xn2
                
            if fi == 0:
                break

            if iter > iter_max:
                break
            
            iter = iter + 1
            iterations.append(iter)
            errors.append(err)
#Error as a function of iterations
        pl.plot(iterations, errors)
        pl.grid()
        pl.xlabel("Number of Iterations")
        pl.ylabel("Error")
        pl.title("Number of Iterations at " "" + str(dT) + "" " K/s")
        pl.show()
        print("Iterations =", iter)
        print("Critical Radius =", Xn2)
        print("Error =", err)
        CR.append(Xn2)
        temp.append(dT)
        list.clear(iterations)
        list.clear(errors)
        
        if len(CR) < 10:
                NR(dT)

    main(X0,tol)
NR(dT)
#Critical radius against temperature
pl.plot(CR, temp)
pl.grid()
pl.xlabel("Critical Radius")
pl.ylabel("Undercooling Rate")
pl.title("How Critical Radius Varies with the Rate of Undercooling in Alloy " "'" + name + "'")
pl.show