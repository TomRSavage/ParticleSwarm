# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 15:59:36 2019

@author: tomsa
"""

import numpy as np 
import copy
import numpy.random as rnd
import time
import matplotlib.pyplot as plt


def Rosenbrock(X):
    '''INPUTS
    X: arguments of the function Rosenbrock
    OUTPUTS
    f : evaluation of the Rosenbrock function given the inputs
    
    DOMAIN         : Xi is within [-5,10] although can be [-2.048,2.048]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=0 x=[1,...,1] 
'''
    f = sum( 100.0*(X[i+1]-X[i]**2)**2 + (1-X[i])**2 for i in range(0,len(X)-1) )
    return f

def Sphere(X):
    '''INPUTS
    X: arguments of the Sphere Function
    OUTPUTS
    f : evaluation of the Sphere function given the inputs
    
    DOMAIN         : [-5.12,5.12]
    DIMENSIONS     : any
    GLOBAL MINIMUM : f(x)=0 x=[0,...,0] 
'''
    f=sum(X[i]**2 for i in range(0,len(X)))
    return f



def initiation(f,bounds,p):
    '''
    INPUTS
    f       :function to be searched over
    bounds  :bounds of function in form [[x1,x2],[x3,x4],[x5,x6]...]
    p       :number of particles
    
    OUTPUTS
    particle_pos      :array of random particle positions 
    particle_best     :array of best particle positions (same as current)
    swarm_best        :coordinates of particle with best known position
    particle_velocity :array of random particle velocity arrays
    local_best        :array of the best particle in each neighbourhood 
    local_best_fitness:function value evaluated at each local best
    particle_pos_val  :fitness of each particle 
    
    '''
    d=len(bounds) #finding number of dimensions
    particle_pos=np.zeros(p) #creating empty position array
    particle_pos=particle_pos.tolist() #converting array to list
    particle_velocity=particle_pos[:] #empty velocity array
    particle_pos_val=particle_pos[:] #empty value array
    for j in range(p): #iterating ovre the number of particles
        particle_pos[j]=[rnd.uniform(bounds[i][0],bounds[i][1])\
                    for i in range(d)] #random coordinate within bounds
        particle_pos_val[j]=f(particle_pos[j]) #calculating function value
                                            #at each particle
        particle_velocity[j]=[rnd.uniform(-abs(bounds[i][1]-bounds[i][0])\
                    ,abs(bounds[i][1]-bounds[i][0])) for i in range(d)]
                    #creating random velocity values for each dimension

    local_best=[0]*p #creating empty local best list
    local_best_fitness=local_best[:]
    for j in range(p):  #finding the best particle in each neighbourhood 
                        #and storing it in 'local_best'
        local_vals=np.zeros(3)
        local_vals[0]=particle_pos_val[j-2]
        local_vals[1]=particle_pos_val[j-1]
        local_vals[2]=particle_pos_val[j]
        min_index=int(np.argmin(local_vals))
        local_best[j]=particle_pos[min_index+j-2][:]
        local_best_fitness[j]=f(local_best[j])

    swarm_best=particle_pos[np.argmin(particle_pos_val)]#getting the lowest particle value
    particle_best=copy.deepcopy(particle_pos)#setting all particles current positions to best
    return d,np.array(particle_pos), np.array(particle_best), \
                 np.array(swarm_best), np.array(particle_velocity), np.array(local_best), \
                     np.array(local_best_fitness),np.array(particle_pos_val)
        
def withinbounds(bounds,particle_pos):
    '''
    DESCRIPTION: 
        Checks whether a particle's position is within the bounds of the problem 
        
    INPUTS
    bounds      :bounds of problem in form [[x1,x2],[x3,x4]...]
    particle_pos:coordinates of a particle e.g [p1,p2,p3...]
    
    OUTPUTS
    inbounds    : True if particle is within bounds and false if outside
    '''
    inbounds=True
    for i in range(len(bounds)):
        if particle_pos[i]<bounds[i][0]:
            inbounds=False
        elif particle_pos[i]>bounds[i][1]:
            inbounds=False
    return inbounds

def trajplot(f_store):
    '''INPUTS:
        f : function for plot(used for contour)
        bounds :bounds over which contour is produced
        f_store : trajectory of function value
    OUTPUTS: 
        plot of function value against iteration
    '''
    it=np.linspace(0,len(f_store),len(f_store))
    plt.figure()
    plt.plot(it,f_store)
    plt.xlabel('Iterations')
    plt.ylabel('Function Value')
    plt.show()
    return



    
                
                
                
                
                
                
                
    