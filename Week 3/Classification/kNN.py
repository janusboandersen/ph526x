#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:29:01 2017

@author: janusboandersen
"""

#k-nearest neighbours (kNN) implementation
import numpy as np
import matplotlib.pyplot as plt
import random

#Simple test data set in R2
points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p = np.array([2.5, 2])

#Slice out 1st column for x-coordinates and 2nd column for y-coordinates

#plt.axis([0.5, 3.5, 0.5, 3.5])

def knn_predict(p, points, k=5):
    #do
#End func def


def find_nearest_neighbours(p, points, k=2):
    """
    From a numpy-array of points, find the k (def. 5) nearest neighbours in Euclidian
    space to the point p. Returns the indices of these neigbours in array points
    Usage:
    >>> p = np.array([1,2])
    >>> points = np.array([[1,1],[1,3],[8,9]])
    >>> find_nearest_neighbours(p,points,k=2)
    >>> 
    """
    
    #Pseudocode to find the k nearest neighbours of point p:
        
    #Ensure k is no larger than available points
    k = min(k, points.shape[0])
    
    #Set up array for measuring distances
    distances = np.zeros(points.shape[0])
        
    #Loop over all neighbour points
    for i in range(len(distances)):
        #Determine the Euclidian distance from the neighbour to the point    
        distances[i] = distance(p, points[i])
    #End for
    
    #Sort distances and return the k points that are nearest to point p
    #Use an indirect sort
    ind = np.argsort(distances)
    #kNN = points[ind[0:k]]
    
    #Plot all points to illustrate
    #plt.plot(points[:,0], points[:,1], "ro")
    #plt.plot(p[0], p[1], "bo")
    
    #Plot k-nearest neighbours
    #plt.plot(kNN[:,0], kNN[:,1], "bs")
    
    #Choose the first k elements
    return ind[:k]

#End func def

#support functions
#Euclidian distance                      
def distance(p1, p2):
    """
    Computes the Euclidian distance between two points p1 and p2.
    The points p1 and p2 should be equal-sized numpy arrays
    """ 
    return np.sqrt(np.sum(np.power(p2-p1, 2)))
#End of function def

def majority_vote(votes):
    """
    Takes a sequence (list, tuple) of votes and returns the majority vote. 
    The item which occurs the most times in the sequence is the majority vote.
    In case of a tied vote, a random item from among the winners will be returned.
    This should in fact be called 'plurality vote'
    """
    #Build dictionary of vote counts to manage the counting process
    vote_counts = {}
    
    #Build list of winner(s) to return the majority vote(s)
    winners = []
    
    #Loop over the sequence
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
        #end if
    #end for
    
    #find the maximum
    max_count = max(vote_counts.values())

    #loop over the hash and unpack each k-v for inspection
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
        #end if
    #end for
    
    return random.choice(winners)
#end function def