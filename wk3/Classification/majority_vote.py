#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:35:49 2017

@author: janusboandersen
"""

#Majority vote for the kNN implementation
import random
import scipy.stats

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


#Alternative implementation using SciPy masked-array stats
def majority_vote2(votes):
    """
    Returns the most scommon element in a sequence (votes).
    Uses scipy.stats.mstats.mode()
    """
    mode, count = scipy.stats.mstats.mode(votes)
    return mode
#end function def


#Try it out
votes = [1,2,3,1,2,3,1,2,3,3,3,3,2,2,2]
print(majority_vote2(votes))